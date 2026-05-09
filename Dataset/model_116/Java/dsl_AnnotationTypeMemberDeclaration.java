





import java.util.List;
import java.util.ArrayList;

public class dsl_AnnotationTypeMemberDeclaration  {

    private String id;





    private dsl_ClassOrInterfaceDeclaration dsl_classorinterfacedeclaration;




    private dsl_AnnotationTypeBody dsl_annotationtypebody;




    private dsl_TypeBodyModifier dsl_typebodymodifier;




    private dsl_AnnotationTypeDeclaration dsl_annotationtypedeclaration;




    private dsl_Type dsl_type;




    private dsl_EnumDeclaration dsl_enumdeclaration;




    private dsl_FieldDeclaration dsl_fielddeclaration;


    public dsl_AnnotationTypeMemberDeclaration(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_ClassOrInterfaceDeclaration getDsl_classorinterfacedeclaration() {
        return dsl_classorinterfacedeclaration;
    }

    public void setDsl_classorinterfacedeclaration(dsl_ClassOrInterfaceDeclaration dsl_classorinterfacedeclaration) {
        this.dsl_classorinterfacedeclaration = dsl_classorinterfacedeclaration;
    }
    public dsl_AnnotationTypeBody getDsl_annotationtypebody() {
        return dsl_annotationtypebody;
    }

    public void setDsl_annotationtypebody(dsl_AnnotationTypeBody dsl_annotationtypebody) {
        this.dsl_annotationtypebody = dsl_annotationtypebody;
    }
    public dsl_TypeBodyModifier getDsl_typebodymodifier() {
        return dsl_typebodymodifier;
    }

    public void setDsl_typebodymodifier(dsl_TypeBodyModifier dsl_typebodymodifier) {
        this.dsl_typebodymodifier = dsl_typebodymodifier;
    }
    public dsl_AnnotationTypeDeclaration getDsl_annotationtypedeclaration() {
        return dsl_annotationtypedeclaration;
    }

    public void setDsl_annotationtypedeclaration(dsl_AnnotationTypeDeclaration dsl_annotationtypedeclaration) {
        this.dsl_annotationtypedeclaration = dsl_annotationtypedeclaration;
    }
    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }
    public dsl_EnumDeclaration getDsl_enumdeclaration() {
        return dsl_enumdeclaration;
    }

    public void setDsl_enumdeclaration(dsl_EnumDeclaration dsl_enumdeclaration) {
        this.dsl_enumdeclaration = dsl_enumdeclaration;
    }
    public dsl_FieldDeclaration getDsl_fielddeclaration() {
        return dsl_fielddeclaration;
    }

    public void setDsl_fielddeclaration(dsl_FieldDeclaration dsl_fielddeclaration) {
        this.dsl_fielddeclaration = dsl_fielddeclaration;
    }

}