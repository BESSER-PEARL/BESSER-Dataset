





import java.util.List;
import java.util.ArrayList;

public class backtrackingContentAssistTest_Expression extends NavigatingExp, OclMessageArg {






    private backtrackingContentAssistTest_Der backtrackingcontentassisttest_der;




    private backtrackingContentAssistTest_Invariant backtrackingcontentassisttest_invariant;




    private backtrackingContentAssistTest_PrefixExp backtrackingcontentassisttest_prefixexp;




    private backtrackingContentAssistTest_InfixExp backtrackingcontentassisttest_infixexp;




    private backtrackingContentAssistTest_Definition backtrackingcontentassisttest_definition;




    private backtrackingContentAssistTest_RoundBracketExp backtrackingcontentassisttest_roundbracketexp;




    private backtrackingContentAssistTest_IfExp backtrackingcontentassisttest_ifexp;




    private backtrackingContentAssistTest_OclMessage backtrackingcontentassisttest_oclmessage;




    private backtrackingContentAssistTest_SquareBracketExp backtrackingcontentassisttest_squarebracketexp;




    private backtrackingContentAssistTest_LetExp backtrackingcontentassisttest_letexp;




    private backtrackingContentAssistTest_CollectionLiteralPart backtrackingcontentassisttest_collectionliteralpart;




    private backtrackingContentAssistTest_IfExp backtrackingcontentassisttest_ifexp;




    private backtrackingContentAssistTest_IfExp backtrackingcontentassisttest_ifexp;




    private backtrackingContentAssistTest_CollectionLiteralPart backtrackingcontentassisttest_collectionliteralpart;




    private backtrackingContentAssistTest_iteratorAccumulator backtrackingcontentassisttest_iteratoraccumulator;




    private backtrackingContentAssistTest_NestedExp backtrackingcontentassisttest_nestedexp;




    private backtrackingContentAssistTest_LetVariable backtrackingcontentassisttest_letvariable;




    private backtrackingContentAssistTest_Body backtrackingcontentassisttest_body;


    public backtrackingContentAssistTest_Expression(
    ) {
        super(
        );
    }



    public backtrackingContentAssistTest_Der getBacktrackingcontentassisttest_der() {
        return backtrackingcontentassisttest_der;
    }

    public void setBacktrackingcontentassisttest_der(backtrackingContentAssistTest_Der backtrackingcontentassisttest_der) {
        this.backtrackingcontentassisttest_der = backtrackingcontentassisttest_der;
    }
    public backtrackingContentAssistTest_Invariant getBacktrackingcontentassisttest_invariant() {
        return backtrackingcontentassisttest_invariant;
    }

    public void setBacktrackingcontentassisttest_invariant(backtrackingContentAssistTest_Invariant backtrackingcontentassisttest_invariant) {
        this.backtrackingcontentassisttest_invariant = backtrackingcontentassisttest_invariant;
    }
    public backtrackingContentAssistTest_PrefixExp getBacktrackingcontentassisttest_prefixexp() {
        return backtrackingcontentassisttest_prefixexp;
    }

    public void setBacktrackingcontentassisttest_prefixexp(backtrackingContentAssistTest_PrefixExp backtrackingcontentassisttest_prefixexp) {
        this.backtrackingcontentassisttest_prefixexp = backtrackingcontentassisttest_prefixexp;
    }
    public backtrackingContentAssistTest_InfixExp getBacktrackingcontentassisttest_infixexp() {
        return backtrackingcontentassisttest_infixexp;
    }

    public void setBacktrackingcontentassisttest_infixexp(backtrackingContentAssistTest_InfixExp backtrackingcontentassisttest_infixexp) {
        this.backtrackingcontentassisttest_infixexp = backtrackingcontentassisttest_infixexp;
    }
    public backtrackingContentAssistTest_Definition getBacktrackingcontentassisttest_definition() {
        return backtrackingcontentassisttest_definition;
    }

    public void setBacktrackingcontentassisttest_definition(backtrackingContentAssistTest_Definition backtrackingcontentassisttest_definition) {
        this.backtrackingcontentassisttest_definition = backtrackingcontentassisttest_definition;
    }
    public backtrackingContentAssistTest_RoundBracketExp getBacktrackingcontentassisttest_roundbracketexp() {
        return backtrackingcontentassisttest_roundbracketexp;
    }

    public void setBacktrackingcontentassisttest_roundbracketexp(backtrackingContentAssistTest_RoundBracketExp backtrackingcontentassisttest_roundbracketexp) {
        this.backtrackingcontentassisttest_roundbracketexp = backtrackingcontentassisttest_roundbracketexp;
    }
    public backtrackingContentAssistTest_IfExp getBacktrackingcontentassisttest_ifexp() {
        return backtrackingcontentassisttest_ifexp;
    }

    public void setBacktrackingcontentassisttest_ifexp(backtrackingContentAssistTest_IfExp backtrackingcontentassisttest_ifexp) {
        this.backtrackingcontentassisttest_ifexp = backtrackingcontentassisttest_ifexp;
    }
    public backtrackingContentAssistTest_OclMessage getBacktrackingcontentassisttest_oclmessage() {
        return backtrackingcontentassisttest_oclmessage;
    }

    public void setBacktrackingcontentassisttest_oclmessage(backtrackingContentAssistTest_OclMessage backtrackingcontentassisttest_oclmessage) {
        this.backtrackingcontentassisttest_oclmessage = backtrackingcontentassisttest_oclmessage;
    }
    public backtrackingContentAssistTest_SquareBracketExp getBacktrackingcontentassisttest_squarebracketexp() {
        return backtrackingcontentassisttest_squarebracketexp;
    }

    public void setBacktrackingcontentassisttest_squarebracketexp(backtrackingContentAssistTest_SquareBracketExp backtrackingcontentassisttest_squarebracketexp) {
        this.backtrackingcontentassisttest_squarebracketexp = backtrackingcontentassisttest_squarebracketexp;
    }
    public backtrackingContentAssistTest_LetExp getBacktrackingcontentassisttest_letexp() {
        return backtrackingcontentassisttest_letexp;
    }

    public void setBacktrackingcontentassisttest_letexp(backtrackingContentAssistTest_LetExp backtrackingcontentassisttest_letexp) {
        this.backtrackingcontentassisttest_letexp = backtrackingcontentassisttest_letexp;
    }
    public backtrackingContentAssistTest_CollectionLiteralPart getBacktrackingcontentassisttest_collectionliteralpart() {
        return backtrackingcontentassisttest_collectionliteralpart;
    }

    public void setBacktrackingcontentassisttest_collectionliteralpart(backtrackingContentAssistTest_CollectionLiteralPart backtrackingcontentassisttest_collectionliteralpart) {
        this.backtrackingcontentassisttest_collectionliteralpart = backtrackingcontentassisttest_collectionliteralpart;
    }
    public backtrackingContentAssistTest_IfExp getBacktrackingcontentassisttest_ifexp() {
        return backtrackingcontentassisttest_ifexp;
    }

    public void setBacktrackingcontentassisttest_ifexp(backtrackingContentAssistTest_IfExp backtrackingcontentassisttest_ifexp) {
        this.backtrackingcontentassisttest_ifexp = backtrackingcontentassisttest_ifexp;
    }
    public backtrackingContentAssistTest_IfExp getBacktrackingcontentassisttest_ifexp() {
        return backtrackingcontentassisttest_ifexp;
    }

    public void setBacktrackingcontentassisttest_ifexp(backtrackingContentAssistTest_IfExp backtrackingcontentassisttest_ifexp) {
        this.backtrackingcontentassisttest_ifexp = backtrackingcontentassisttest_ifexp;
    }
    public backtrackingContentAssistTest_CollectionLiteralPart getBacktrackingcontentassisttest_collectionliteralpart() {
        return backtrackingcontentassisttest_collectionliteralpart;
    }

    public void setBacktrackingcontentassisttest_collectionliteralpart(backtrackingContentAssistTest_CollectionLiteralPart backtrackingcontentassisttest_collectionliteralpart) {
        this.backtrackingcontentassisttest_collectionliteralpart = backtrackingcontentassisttest_collectionliteralpart;
    }
    public backtrackingContentAssistTest_iteratorAccumulator getBacktrackingcontentassisttest_iteratoraccumulator() {
        return backtrackingcontentassisttest_iteratoraccumulator;
    }

    public void setBacktrackingcontentassisttest_iteratoraccumulator(backtrackingContentAssistTest_iteratorAccumulator backtrackingcontentassisttest_iteratoraccumulator) {
        this.backtrackingcontentassisttest_iteratoraccumulator = backtrackingcontentassisttest_iteratoraccumulator;
    }
    public backtrackingContentAssistTest_NestedExp getBacktrackingcontentassisttest_nestedexp() {
        return backtrackingcontentassisttest_nestedexp;
    }

    public void setBacktrackingcontentassisttest_nestedexp(backtrackingContentAssistTest_NestedExp backtrackingcontentassisttest_nestedexp) {
        this.backtrackingcontentassisttest_nestedexp = backtrackingcontentassisttest_nestedexp;
    }
    public backtrackingContentAssistTest_LetVariable getBacktrackingcontentassisttest_letvariable() {
        return backtrackingcontentassisttest_letvariable;
    }

    public void setBacktrackingcontentassisttest_letvariable(backtrackingContentAssistTest_LetVariable backtrackingcontentassisttest_letvariable) {
        this.backtrackingcontentassisttest_letvariable = backtrackingcontentassisttest_letvariable;
    }
    public backtrackingContentAssistTest_Body getBacktrackingcontentassisttest_body() {
        return backtrackingcontentassisttest_body;
    }

    public void setBacktrackingcontentassisttest_body(backtrackingContentAssistTest_Body backtrackingcontentassisttest_body) {
        this.backtrackingcontentassisttest_body = backtrackingcontentassisttest_body;
    }

}