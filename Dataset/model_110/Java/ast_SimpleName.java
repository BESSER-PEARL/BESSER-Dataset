





import java.util.List;
import java.util.ArrayList;

public class ast_SimpleName extends Name {

    private String identifier;





    private ast_MethodInvocation ast_methodinvocation;




    private ast_MemberRef ast_memberref;




    private ast_MethodRef ast_methodref;




    private ast_SuperMethodInvocation ast_supermethodinvocation;




    private ast_FieldAccess ast_fieldaccess;




    private ast_SuperFieldAccess ast_superfieldaccess;




    private ast_MemberValuePair ast_membervaluepair;


    public ast_SimpleName(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ast_MethodInvocation getAst_methodinvocation() {
        return ast_methodinvocation;
    }

    public void setAst_methodinvocation(ast_MethodInvocation ast_methodinvocation) {
        this.ast_methodinvocation = ast_methodinvocation;
    }
    public ast_MemberRef getAst_memberref() {
        return ast_memberref;
    }

    public void setAst_memberref(ast_MemberRef ast_memberref) {
        this.ast_memberref = ast_memberref;
    }
    public ast_MethodRef getAst_methodref() {
        return ast_methodref;
    }

    public void setAst_methodref(ast_MethodRef ast_methodref) {
        this.ast_methodref = ast_methodref;
    }
    public ast_SuperMethodInvocation getAst_supermethodinvocation() {
        return ast_supermethodinvocation;
    }

    public void setAst_supermethodinvocation(ast_SuperMethodInvocation ast_supermethodinvocation) {
        this.ast_supermethodinvocation = ast_supermethodinvocation;
    }
    public ast_FieldAccess getAst_fieldaccess() {
        return ast_fieldaccess;
    }

    public void setAst_fieldaccess(ast_FieldAccess ast_fieldaccess) {
        this.ast_fieldaccess = ast_fieldaccess;
    }
    public ast_SuperFieldAccess getAst_superfieldaccess() {
        return ast_superfieldaccess;
    }

    public void setAst_superfieldaccess(ast_SuperFieldAccess ast_superfieldaccess) {
        this.ast_superfieldaccess = ast_superfieldaccess;
    }
    public ast_MemberValuePair getAst_membervaluepair() {
        return ast_membervaluepair;
    }

    public void setAst_membervaluepair(ast_MemberValuePair ast_membervaluepair) {
        this.ast_membervaluepair = ast_membervaluepair;
    }

}