v='package'
u='language'
t='stdout'
s='encoding'
r='stdin'
q='command'
p='--stack'
o='Case 3'
n='--check'
m='s0 s1 s2 s3\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s3\ns1 0 s3\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns3 0 s3\ns3 1 s0'
i='verify'
h='prepare'
g='find'
f='cwd'
e='utf-8'
d='\n'
c='languageCommand'
b='--mini'
a=open
X='setup'
W=None
V='--det'
U=False
T='Case 2'
S='Case 1'
P='root'
O=True
N='cases'
M='enabled'
J=print
I='arguments'
G='testType'
E='output'
D='inputType'
B='input'
A='name'
from enum import Enum as Y
import tempfile as Z,subprocess as L,multiprocessing as w,copy,sys as Q,os as F
class C(Y):FILE=0;CONSOLE=1
class H(Y):TEST_EQUAL=0
class R(Y):PYTHON=0;CPP=1
x='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
y='IGEN\nNEM\nIGEN\nIGEN\nNEM'
z='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
A0='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
A1='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
A2='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
A3='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
A4='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
A5='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
A6='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
A7='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
A8='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
A9='q0 q1 q2 q3 q4 q5\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q4\nq1 0 q4\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q5\nq3 1 q4\nq4 0 q4\nq4 1 q3\nq5 0 q4\nq5 1 q2'
AA='s0 s1 s2 s4\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s4\ns1 0 s4\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns4 0 s4\ns4 1 s0'
AB=m
AC='q0 q1 q2 q3\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q3\nq1 0 q3\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q3\nq3 1 q0'
AD=m
AE='q0 q1 q2\n0 1\nq0\nq0 q2\nq0 0 q1\nq0 1 q2\nq1 0 q1\nq1 1 q2\nq2 0 q1\nq2 1 q2'
AF='s0 s1\n0 1\ns0\ns0\ns0 0 s1\ns0 1 s0\ns1 0 s1\ns1 1 s0'
AG='q0 q1 q2\na b\nz0 z1\nq0\nz0\nq0\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 E z0 E q0'
AH='IGEN\nNEM\nNEM\nNEM\nNEM\nNEM'
AI='q0 q1 q2 q3\na b\nz0 z1\nq0\nz0\nq3\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 b z0 z0z0 q2\nq2 E z0 E q0'
AJ='IGEN\nIGEN\nNEM\nNEM\nNEM'
AK=[{A:'Problem 1 (DFA - Deterministic Finite Automaton)',M:O,N:[{A:S,D:C.FILE,G:H.TEST_EQUAL,B:x,E:y,I:[n,'10101,111,111110111010101,001,0021']},{A:T,D:C.FILE,G:H.TEST_EQUAL,B:z,E:A0,I:[n,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]},{A:'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',M:U,N:[{A:S,D:C.FILE,G:H.TEST_EQUAL,B:A1,E:A2,I:[V]},{A:T,D:C.FILE,G:H.TEST_EQUAL,B:A3,E:A4,I:[V]},{A:o,D:C.FILE,G:H.TEST_EQUAL,B:A5,E:A6,I:[V]},{A:'Case 4',D:C.FILE,G:H.TEST_EQUAL,B:A7,E:A8,I:[V]}]},{A:'Problem 3 (Minimizing a Finite Automaton)',M:U,N:[{A:S,D:C.FILE,G:H.TEST_EQUAL,B:A9,E:[AA,AB],I:[b]},{A:T,D:C.FILE,G:H.TEST_EQUAL,B:AC,E:AD,I:[b]},{A:o,D:C.FILE,G:H.TEST_EQUAL,B:AE,E:AF,I:[b]}]},{A:'Problem 4 (Stack Automaton)',M:U,N:[{A:S,D:C.FILE,G:H.TEST_EQUAL,B:AG,E:AH,I:[p,'aabb,abb,aab,abab,a,b']},{A:T,D:C.FILE,G:H.TEST_EQUAL,B:AI,E:AJ,I:[p,'ab,abb,aaabb,a,b']}]}]
class K(Exception):0
def j():return F.path.join(Z._get_default_tempdir(),next(Z._get_candidate_names()))
def AL(environment,case):
	F=case;A=environment;G=copy.deepcopy(A[c]);H=F.get(I,[])
	if F[D]==C.FILE:G.extend(['--input',A[B],'--output',A[E]])
	if F[D]==C.CONSOLE:J=F[B]+d;K=e
	else:J=W;K=W
	if H:G.extend(H)
	A[q]=G;A[r]=J;A[s]=K
def AM(environment,case):
	A=environment;AL(A,case)
	try:
		B=L.run(A[q],cwd=A[f],capture_output=O,text=O,input=A[r],encoding=A[s])
		for C in[B.stdout,B.stderr]:
			if C:
				C=C.strip()
				if C:J(C.strip())
		if B.returncode!=0:raise K(f"Program exited with status code {B.returncode}")
		A[t]=B.stdout.strip()
	except L.CalledProcessError as D:raise K(f"Couldn't run project: {D}")
def AN(folder):
	for(A,G,B)in F.walk(folder):
		for C in B:
			if C=='__main__.py':D=F.path.dirname(A);E=F.path.basename(A);return{u:R.PYTHON,P:D,v:E}
def AO(folder):
	for(A,D,B)in F.walk(folder):
		for C in B:
			if C=='CMakeLists.txt':return{u:R.CPP,P:A}
def AP(folder):
	for(B,G,C)in F.walk(folder):
		for D in C:
			A=F.path.join(B,D)
			try:
				with a(A,'rb')as E:
					if E.read(4)==b'\x7fELF':return A
			except:pass
def AQ(environment):A=environment;B=A[v];A[f]=A[P];A[c]=['python3','-m',B]
def AR(environment):
	B=environment;A=Z.mkdtemp()
	try:L.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[P]],cwd=A,check=O)
	except L.CalledProcessError as D:raise K(f"Could not configure CMake project")
	try:L.run(['make','-j',str(w.cpu_count())],cwd=A)
	except L.CalledProcessError as D:raise K(f"Could not build CMake project")
	C=AP(A)
	if not C:raise K(f"Couldn't find built executable in CMake project")
	B[f]=A;B[c]=[C]
def AS(case,environment):
	A=environment;C=j();D=j();A[B]=C;A[E]=D
	with a(C,'w',encoding=e)as F:F.write(case[B])
def AT(case,environment):
	C=environment;D=C[B];A=C[E]
	if not F.path.exists(A):raise K(f"Output file not created by program")
	with a(A,'r',encoding=e)as H:I=H.read().strip()
	if not l[case[G]](case,I):raise K(f"Output mismatch: expected different output in file")
	if F.path.exists(D):F.remove(D)
	if F.path.exists(A):F.remove(A)
def AU(case,environment):
	if not l[case[G]](case,environment[t]):raise K(f"Output mismatch: expected different output on stdout")
def k(text):return d.join([A.strip()for A in text.strip().split(d)])
def AV(case,output):B=k(output);A=case[E];C=[A]if isinstance(A,str)else A;return any([k(A)==B for A in C])
AW={R.PYTHON:{A:'Python',g:AN,h:AQ},R.CPP:{A:'CMake (C++)',g:AO,h:AR}}
AX={C.FILE:{X:AS,i:AT},C.CONSOLE:{X:W,i:AU}}
l={H.TEST_EQUAL:AV}
def AY():
	R=F.getcwd();B=W
	for(S,E)in AW.items():
		B=E[g](R)
		if B:break
	if not B:J("❌ Couldn't find any project in the current folder ❌");Q.exit(1)
	J(f"Found {E[A]} project in {B[P]}")
	try:E[h](B)
	except K as G:J(f"❌ Error during build: {G}");Q.exit(2)
	J('Running tests...');L=U
	for H in AK:
		if not H[M]:continue
		J(f"Problem: {H[A]}")
		for C in H[N]:
			J(f"Running case: {C[A]}")
			try:
				I=AX[C[D]]
				if I[X]:I[X](C,B)
				AM(B,C)
				if C[D]:I[i](C,B)
			except K as G:J(f"❌ Failed {C[A]}: {G} ❌");L=O;continue
			J(f"🎉 {C[A]} succeeded 🎉")
	if L:J('❌ Some tests failed. ❌');Q.exit(3)
	J('🎉 All tests passed! Congratulations! 🎉');Q.exit(0)
if __name__=='__main__':AY()