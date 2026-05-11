





import java.util.List;
import java.util.ArrayList;

public class myDsl_Type_declaration  {

    private String comment;





    private myDsl_Compilation_unit mydsl_compilation_unit;


    public myDsl_Type_declaration(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public myDsl_Compilation_unit getMydsl_compilation_unit() {
        return mydsl_compilation_unit;
    }

    public void setMydsl_compilation_unit(myDsl_Compilation_unit mydsl_compilation_unit) {
        this.mydsl_compilation_unit = mydsl_compilation_unit;
    }

}