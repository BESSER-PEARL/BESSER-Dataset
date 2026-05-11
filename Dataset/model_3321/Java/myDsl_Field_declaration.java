





import java.util.List;
import java.util.ArrayList;

public class myDsl_Field_declaration  {

    private String comment;





    private myDsl_Interface_declaration mydsl_interface_declaration;




    private myDsl_Class_declaration mydsl_class_declaration;


    public myDsl_Field_declaration(
        String comment    ) {
        this.comment = comment;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public myDsl_Interface_declaration getMydsl_interface_declaration() {
        return mydsl_interface_declaration;
    }

    public void setMydsl_interface_declaration(myDsl_Interface_declaration mydsl_interface_declaration) {
        this.mydsl_interface_declaration = mydsl_interface_declaration;
    }
    public myDsl_Class_declaration getMydsl_class_declaration() {
        return mydsl_class_declaration;
    }

    public void setMydsl_class_declaration(myDsl_Class_declaration mydsl_class_declaration) {
        this.mydsl_class_declaration = mydsl_class_declaration;
    }

}