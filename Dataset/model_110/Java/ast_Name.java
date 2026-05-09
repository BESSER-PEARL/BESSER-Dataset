





import java.util.List;
import java.util.ArrayList;

public class ast_Name extends Expression, IDocElement {






    private ast_NormalAnnotation ast_normalannotation;




    private ast_SingleMemberAnnotation ast_singlememberannotation;




    private ast_MarkerAnnotation ast_markerannotation;


    public ast_Name(
    ) {
        super(
        );
    }



    public ast_NormalAnnotation getAst_normalannotation() {
        return ast_normalannotation;
    }

    public void setAst_normalannotation(ast_NormalAnnotation ast_normalannotation) {
        this.ast_normalannotation = ast_normalannotation;
    }
    public ast_SingleMemberAnnotation getAst_singlememberannotation() {
        return ast_singlememberannotation;
    }

    public void setAst_singlememberannotation(ast_SingleMemberAnnotation ast_singlememberannotation) {
        this.ast_singlememberannotation = ast_singlememberannotation;
    }
    public ast_MarkerAnnotation getAst_markerannotation() {
        return ast_markerannotation;
    }

    public void setAst_markerannotation(ast_MarkerAnnotation ast_markerannotation) {
        this.ast_markerannotation = ast_markerannotation;
    }

}