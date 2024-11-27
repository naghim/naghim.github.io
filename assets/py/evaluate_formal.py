t='package'
s='language'
r='stdout'
q='encoding'
p='stdin'
o='command'
n='--stack'
m='Case 3'
l='--check'
k='s0 s1 s2 s3\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s3\ns1 0 s3\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns3 0 s3\ns3 1 s0'
g='verify'
f='prepare'
e='find'
d='cwd'
c='utf-8'
b='\n'
a='languageCommand'
Z='--mini'
Y=open
V='setup'
U=True
T=None
S='--det'
R='Case 2'
Q='Case 1'
N='root'
M='cases'
J=print
I='arguments'
G='testType'
E='output'
D='inputType'
B='input'
A='name'
from enum import Enum as W
import tempfile as X,subprocess as L,multiprocessing as u,copy,sys as O,os as F
class C(W):FILE=0;CONSOLE=1
class H(W):TEST_EQUAL=0
class P(W):PYTHON=0;CPP=1
v='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
w='IGEN\nNEM\nIGEN\nIGEN\nNEM'
x='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
y='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
z='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
A0='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
A1='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
A2='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
A3='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
A4='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
A5='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
A6='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
A7='q0 q1 q2 q3 q4 q5\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q4\nq1 0 q4\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q5\nq3 1 q4\nq4 0 q4\nq4 1 q3\nq5 0 q4\nq5 1 q2'
A8='s0 s1 s2 s4\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s4\ns1 0 s4\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns4 0 s4\ns4 1 s0'
A9=k
AA='q0 q1 q2 q3\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q3\nq1 0 q3\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q3\nq3 1 q0'
AB=k
AC='q0 q1 q2\n0 1\nq0\nq0 q2\nq0 0 q1\nq0 1 q2\nq1 0 q1\nq1 1 q2\nq2 0 q1\nq2 1 q2'
AD='s0 s1\n0 1\ns0\ns0\ns0 0 s1\ns0 1 s0\ns1 0 s1\ns1 1 s0'
AE='q0 q1 q2\na b\nz0 z1\nq0\nz0\nq0\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 E z0 E q0'
AF='IGEN\nNEM\nNEM\nNEM\nNEM\nNEM'
AG='q0 q1 q2 q3\na b\nz0 z1\nq0\nz0\nq3\nq0 a z0 z0z1 q1\nq1 a z1 z1z1 q1\nq1 b z1 E q2\nq2 b z1 E q2\nq2 b z0 z0z0 q2\nq2 E z0 E q0'
AH='IGEN\nIGEN\nNEM\nNEM\nNEM'
AI=[{A:'Problem 1 (DFA - Deterministic Finite Automaton)',M:[{A:Q,D:C.FILE,G:H.TEST_EQUAL,B:v,E:w,I:[l,'10101,111,111110111010101,001,0021']},{A:R,D:C.FILE,G:H.TEST_EQUAL,B:x,E:y,I:[l,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]},{A:'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',M:[{A:Q,D:C.FILE,G:H.TEST_EQUAL,B:z,E:A0,I:[S]},{A:R,D:C.FILE,G:H.TEST_EQUAL,B:A1,E:A2,I:[S]},{A:m,D:C.FILE,G:H.TEST_EQUAL,B:A3,E:A4,I:[S]},{A:'Case 4',D:C.FILE,G:H.TEST_EQUAL,B:A5,E:A6,I:[S]}]},{A:'Problem 3 (Minimizing a Finite Automaton)',M:[{A:Q,D:C.FILE,G:H.TEST_EQUAL,B:A7,E:[A8,A9],I:[Z]},{A:R,D:C.FILE,G:H.TEST_EQUAL,B:AA,E:AB,I:[Z]},{A:m,D:C.FILE,G:H.TEST_EQUAL,B:AC,E:AD,I:[Z]}]},{A:'Problem 4 (Stack Automaton)',M:[{A:Q,D:C.FILE,G:H.TEST_EQUAL,B:AE,E:AF,I:[n,'aabb,abb,aab,abab,a,b']},{A:R,D:C.FILE,G:H.TEST_EQUAL,B:AG,E:AH,I:[n,'ab,abb,aaabb,a,b']}]}]
class K(Exception):0
def h():return F.path.join(X._get_default_tempdir(),next(X._get_candidate_names()))
def AJ(environment,case):
	F=case;A=environment;G=copy.deepcopy(A[a]);H=F.get(I,[])
	if F[D]==C.FILE:G.extend(['--input',A[B],'--output',A[E]])
	if F[D]==C.CONSOLE:J=F[B]+b;K=c
	else:J=T;K=T
	if H:G.extend(H)
	A[o]=G;A[p]=J;A[q]=K
def AK(environment,case):
	A=environment;AJ(A,case)
	try:
		B=L.run(A[o],cwd=A[d],capture_output=U,text=U,input=A[p],encoding=A[q])
		for C in[B.stdout,B.stderr]:
			if C:
				C=C.strip()
				if C:J(C.strip())
		if B.returncode!=0:raise K(f"Program exited with status code {B.returncode}")
		A[r]=B.stdout.strip()
	except L.CalledProcessError as D:raise K(f"Couldn't run project: {D}")
def AL(folder):
	for(A,G,B)in F.walk(folder):
		for C in B:
			if C=='__main__.py':D=F.path.dirname(A);E=F.path.basename(A);return{s:P.PYTHON,N:D,t:E}
def AM(folder):
	for(A,D,B)in F.walk(folder):
		for C in B:
			if C=='CMakeLists.txt':return{s:P.CPP,N:A}
def AN(folder):
	for(B,G,C)in F.walk(folder):
		for D in C:
			A=F.path.join(B,D)
			try:
				with Y(A,'rb')as E:
					if E.read(4)==b'\x7fELF':return A
			except:pass
def AO(environment):A=environment;B=A[t];A[d]=A[N];A[a]=['python3','-m',B]
def AP(environment):
	B=environment;A=X.mkdtemp()
	try:L.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[N]],cwd=A,check=U)
	except L.CalledProcessError as D:raise K(f"Could not configure CMake project")
	try:L.run(['make','-j',str(u.cpu_count())],cwd=A)
	except L.CalledProcessError as D:raise K(f"Could not build CMake project")
	C=AN(A)
	if not C:raise K(f"Couldn't find built executable in CMake project")
	B[d]=A;B[a]=[C]
def AQ(case,environment):
	A=environment;C=h();D=h();A[B]=C;A[E]=D
	with Y(C,'w',encoding=c)as F:F.write(case[B])
def AR(case,environment):
	C=environment;D=C[B];A=C[E]
	if not F.path.exists(A):raise K(f"Output file not created by program")
	with Y(A,'r',encoding=c)as H:I=H.read().strip()
	if not j[case[G]](case,I):raise K(f"Output mismatch: expected different output in file")
	if F.path.exists(D):F.remove(D)
	if F.path.exists(A):F.remove(A)
def AS(case,environment):
	if not j[case[G]](case,environment[r]):raise K(f"Output mismatch: expected different output on stdout")
def i(text):return b.join([A.strip()for A in text.strip().split(b)])
def AT(case,output):B=i(output);A=case[E];C=[A]if isinstance(A,str)else A;return any([i(A)==B for A in C])
AU={P.PYTHON:{A:'Python',e:AL,f:AO},P.CPP:{A:'CMake (C++)',e:AM,f:AP}}
AV={C.FILE:{V:AQ,g:AR},C.CONSOLE:{V:T,g:AS}}
j={H.TEST_EQUAL:AT}
def AW():
	P=F.getcwd();B=T
	for(Q,E)in AU.items():
		B=E[e](P)
		if B:break
	if not B:J("❌ Couldn't find any project in the current folder ❌");O.exit(1)
	J(f"Found {E[A]} project in {B[N]}")
	try:E[f](B)
	except K as G:J(f"❌ Error during build: {G}");O.exit(2)
	J('Running tests...');I=False
	for L in AI:
		J(f"Problem: {L[A]}")
		for C in L[M]:
			J(f"Running case: {C[A]}")
			try:
				H=AV[C[D]]
				if H[V]:H[V](C,B)
				AK(B,C)
				if C[D]:H[g](C,B)
			except K as G:J(f"❌ Failed {C[A]}: {G} ❌");I=U;continue
			J(f"🎉 {C[A]} succeeded 🎉")
	if I:J('❌ Some tests failed. ❌');O.exit(3)
	J('🎉 All tests passed! Congratulations! 🎉');O.exit(0)
if __name__=='__main__':AW()