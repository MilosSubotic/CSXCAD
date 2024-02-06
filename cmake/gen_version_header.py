#!/usr/bin/env python

import re
import sys
v = sys.argv[1]
m = re.match(r'v(\d+)\.(\d+)\.(\d+)(-(\d+)-(\w+))?', v)
v_major = m[1]
v_minor = m[2]
v_patch = m[3]
v_commit = m[5] or 0
print('''
#ifndef CSXCAD_VERSION_H_
#define CSXCAD_VERSION_H_
#define _CSXCAD_VERSION_ "{}"
#define CSXCAD_VERSION_CTOR(major, minor, patch, commit) \\
	( \\
		(0LL|(major)) << 16*3 | \\
		(0LL|(minor)) << 16*2 | \\
		(0LL|(patch)) << 16*1 | \\
		(0LL|(commit)) \\
	) 
#define CSXCAD_VERSION CSXCAD_VERSION_CTOR({}, {}, {}, {})
#endif /*CSXCAD_VERSION_H_*/
'''.format(v, v_major, v_minor, v_patch, v_commit))
