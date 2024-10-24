r='package'
q='language'
p='stdout'
o='encoding'
n='stdin'
m='command'
l='Case 3'
k='--check'
g='verify'
f='prepare'
e='find'
d='cwd'
c='utf-8'
b='\n'
a='languageCommand'
Z='--mini'
Y='Case 2'
X='Case 1'
W=open
T='setup'
S=True
R=None
Q='--det'
P='cases'
M='root'
K='arguments'
H='testType'
G=print
F='output'
E='inputType'
B='input'
A='name'
from enum import Enum as U
import tempfile as V,subprocess as L,multiprocessing as s,copy,sys as N,os as C
class D(U):FILE=0;CONSOLE=1
class I(U):TEST_EQUAL=0
class O(U):PYTHON=0;CPP=1
t='q0 q1 q2\n0 1\nq0\nq0\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q0\nq2 0 q1\nq2 1 q2'
u='IGEN\nNEM\nIGEN\nIGEN\nNEM'
v='q0 q1 q2\na b\nq0\nq1 q2\nq0 a q1\nq1 a q1\nq1 b q2\nq2 b q2'
w='IGEN\nIGEN\nNEM\nNEM\nIGEN\nIGEN\nNEM\nNEM'
x='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q1\nq0 0 q2\nq0 1 q1\nq1 0 q2\nq1 1 q2'
y='s0 s1 s2 s3\n0 1\ns0\ns1 s3\ns0 0 s1\ns0 1 s2\ns1 0 s3\ns1 1 s3\ns2 0 s3\ns2 1 s3'
z='q0 q1 q2\n0 1\nq0\nq2\nq0 0 q0\nq0 0 q1\nq0 1 q0\nq0 1 q1\nq1 0 q1\nq1 0 q2\nq1 1 q0\nq1 1 q1\nq1 1 q2\nq2 0 q1'
A0='s0 s1 s2\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s1\ns1 0 s2\ns1 1 s2\ns2 0 s2\ns2 1 s2'
A1='q0 q1 q2 q3\n0 1\nq0\nq1 q3\nq0 0 q2\nq0 1 q1\nq1 0 q1\nq1 1 q2\nq1 1 q3\nq2 1 q2\nq3 0 q2\nq3 0 q3\nq3 1 q2'
A2='s0 s1 s2 s3\n0 1\ns0\ns2 s3\ns0 0 s1\ns0 1 s2\ns1 1 s1\ns2 0 s2\ns2 1 s3\ns3 0 s3\ns3 1 s1'
A3='q0 q1\n0 1\nq0\nq1\nq0 0 q0\nq0 1 q1\nq1 0 q0\nq1 1 q1'
A4='s0 s1\n0 1\ns0\ns1\ns0 0 s0\ns0 1 s1\ns1 0 s0\ns1 1 s1'
A5='q0 q1 q2 q3 q4 q5\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q4\nq1 0 q4\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q5\nq3 1 q4\nq4 0 q4\nq4 1 q3\nq5 0 q4\nq5 1 q2'
A6='s0 s1 s2 s4\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s4\ns1 0 s4\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns4 0 s4\ns4 1 s0'
A7='q0 q1 q2 q3\n0 1\nq0\nq2\nq0 0 q1\nq0 1 q3\nq1 0 q3\nq1 1 q2\nq2 0 q0\nq2 1 q2\nq3 0 q3\nq3 1 q0'
A8='s0 s1 s2 s3\n0 1\ns0\ns2\ns0 0 s1\ns0 1 s3\ns1 0 s3\ns1 1 s2\ns2 0 s0\ns2 1 s2\ns3 0 s3\ns3 1 s0'
A9='q0 q1 q2\n0 1\nq0\nq0 q2\nq0 0 q1\nq0 1 q2\nq1 0 q1\nq1 1 q2\nq2 0 q1\nq2 1 q2'
AA='s0 s1\n0 1\ns0\ns0\ns0 0 s1\ns0 1 s0\ns1 0 s1\ns1 1 s0'
AB=[{A:'Problem 1 (DFA - Deterministic Finite Automaton)',P:[{A:X,E:D.FILE,H:I.TEST_EQUAL,B:t,F:u,K:[k,'10101,111,111110111010101,001,0021']},{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:v,F:w,K:[k,'a,aa,abab,bbb,aaaaaaaaaaaab,aaaaabbbbb,aaaabbbbba,c']}]},{A:'Problem 2 (Transforming a Non-Deterministic Finite Automata Into a Deterministic One)',P:[{A:X,E:D.FILE,H:I.TEST_EQUAL,B:x,F:y,K:[Q]},{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:z,F:A0,K:[Q]},{A:l,E:D.FILE,H:I.TEST_EQUAL,B:A1,F:A2,K:[Q]},{A:'Case 4',E:D.FILE,H:I.TEST_EQUAL,B:A3,F:A4,K:[Q]}]},{A:'Problem 3 (Minimizing a Finite Automaton)',P:[{A:X,E:D.FILE,H:I.TEST_EQUAL,B:A5,F:A6,K:[Z]},{A:Y,E:D.FILE,H:I.TEST_EQUAL,B:A7,F:A8,K:[Z]},{A:l,E:D.FILE,H:I.TEST_EQUAL,B:A9,F:AA,K:[Z]}]}]
class J(Exception):0
def h():return C.path.join(V._get_default_tempdir(),next(V._get_candidate_names()))
def AC(environment,case):
	C=case;A=environment;G=copy.deepcopy(A[a]);H=C.get(K,[])
	if C[E]==D.FILE:G.extend(['--input',A[B],'--output',A[F]])
	if C[E]==D.CONSOLE:I=C[B]+b;J=c
	else:I=R;J=R
	if H:G.extend(H)
	A[m]=G;A[n]=I;A[o]=J
def AD(environment,case):
	A=environment;AC(A,case)
	try:
		B=L.run(A[m],cwd=A[d],capture_output=S,text=S,input=A[n],encoding=A[o])
		for C in[B.stdout,B.stderr]:
			if C:
				C=C.strip()
				if C:G(C.strip())
		if B.returncode!=0:raise J(f"Program exited with status code {B.returncode}")
		A[p]=B.stdout.strip()
	except L.CalledProcessError as D:raise J(f"Couldn't run project: {D}")
def AE(folder):
	for(A,G,B)in C.walk(folder):
		for D in B:
			if D=='__main__.py':E=C.path.dirname(A);F=C.path.basename(A);return{q:O.PYTHON,M:E,r:F}
def AF(folder):
	for(A,E,B)in C.walk(folder):
		for D in B:
			if D=='CMakeLists.txt':return{q:O.CPP,M:A}
def AG(folder):
	for(B,G,D)in C.walk(folder):
		for E in D:
			A=C.path.join(B,E)
			try:
				with W(A,'rb')as F:
					if F.read(4)==b'\x7fELF':return A
			except:pass
def AH(environment):A=environment;B=A[r];A[d]=A[M];A[a]=['python3','-m',B]
def AI(environment):
	B=environment;A=V.mkdtemp()
	try:L.run(['cmake','-DCMAKE_BUILD_TYPE=Release',B[M]],cwd=A,check=S)
	except L.CalledProcessError as D:raise J(f"Could not configure CMake project")
	try:L.run(['make','-j',str(s.cpu_count())],cwd=A)
	except L.CalledProcessError as D:raise J(f"Could not build CMake project")
	C=AG(A)
	if not C:raise J(f"Couldn't find built executable in CMake project")
	B[d]=A;B[a]=[C]
def AJ(case,environment):
	A=environment;C=h();D=h();A[B]=C;A[F]=D
	with W(C,'w',encoding=c)as E:E.write(case[B])
def AK(case,environment):
	D=environment;E=D[B];A=D[F]
	if not C.path.exists(A):raise J(f"Output file not created by program")
	with W(A,'r',encoding=c)as G:I=G.read().strip()
	if not j[case[H]](case,I):raise J(f"Output mismatch: expected different output in file")
	if C.path.exists(E):C.remove(E)
	if C.path.exists(A):C.remove(A)
def AL(case,environment):
	if not j[case[H]](case,environment[p]):raise J(f"Output mismatch: expected different output on stdout")
def i(text):return b.join([A.strip()for A in text.split(b)])
def AM(case,output):return i(output.strip())==i(case[F].strip())
AN={O.PYTHON:{A:'Python',e:AE,f:AH},O.CPP:{A:'CMake (C++)',e:AF,f:AI}}
AO={D.FILE:{T:AJ,g:AK},D.CONSOLE:{T:R,g:AL}}
j={I.TEST_EQUAL:AM}
def AP():
	O=C.getcwd();B=R
	for(Q,F)in AN.items():
		B=F[e](O)
		if B:break
	if not B:G("❌ Couldn't find any project in the current folder ❌");N.exit(1)
	G(f"Found {F[A]} project in {B[M]}")
	try:F[f](B)
	except J as H:G(f"❌ Error during build: {H}");N.exit(2)
	G('Running tests...');K=False
	for L in AB:
		G(f"Problem: {L[A]}")
		for D in L[P]:
			G(f"Running case: {D[A]}")
			try:
				I=AO[D[E]]
				if I[T]:I[T](D,B)
				AD(B,D)
				if D[E]:I[g](D,B)
			except J as H:G(f"❌ Failed {D[A]}: {H} ❌");K=S;continue
			G(f"🎉 {D[A]} succeeded 🎉")
	if K:G('❌ Some tests failed. ❌');N.exit(3)
	G('🎉 All tests passed! Congratulations! 🎉');N.exit(0)
if __name__=='__main__':AP()
