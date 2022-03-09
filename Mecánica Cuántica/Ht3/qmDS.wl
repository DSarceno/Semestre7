(* ::Package:: *)

(* :Author: Diego Sarce\[NTilde]o *)
(* :Date: March 07, 2022 *)
(* :Description: Package with useful routines in quantum mechanics *)
BeginPackage["qmDS`"]

ObservableEV::usage="ObservableEV[SqMatrix,Eigenvalue] gives de set of eigenvectors asociated to the given eigenvalue."
Proyector::usage="Proyector[Vector] constructs the ket-bra using the same vector."
ExpectationValue::usage="ExpectationValue[SqMatrix,State] gives the expectation value of an observable and a quantum state."
Conmutator::usage="Conmutator[SqMatrix1,SqMatrix2] constructs the conmutator between two observables."
GeneralProbability::usage="GeneralProbability[SqMatrix,State,Eigenvalue] gives the probability to find the state in the given eigenvalue by applying the observable."


Begin["`Private`"]
(* ObservableEV *)
ObservableEV[SqMatrix_,EigValue_]:=Eigenvectors[SqMatrix][[Flatten[Position[Eigenvalues[SqMatrix],EigValue]]]]


(* Proyector *)
Proyector[Vector_]:=Outer[Times,Vector,Conjugate[Vector]]


(* ExpectationValue *)
ExpectationValue[SqMatrix_,State_]:=Conjugate[State] . (SqMatrix . State)


(* Conmutator *)
Conmutator[SqMatrix1_,SqMatrix2_]:=SqMatrix1 . SqMatrix2 - SqMatrix2 . SqMatrix1


(* GeneralProbability *)
GeneralProbability[SqMatrix_,State_,Eigenvalue_]:=Piecewise[{{(Abs[# . State]^2)/(Norm[#]^2*Norm[State]^2)&/@Eigensystem[SqMatrix][[2,Position[Eigensystem[SqMatrix][[1]],Eigenvalue][[1]]]],Count[Eigenvalues[SqMatrix],Eigenvalue]==1},{Total[Abs[# . State]^2/(Norm[#]^2*Norm[State]^2)&/@ObservableEV[SqMatrix,Eigenvalue]],Count[Eigenvalues[SqMatrix],Eigenvalue]>1}}]


End[];
EndPackage[]
