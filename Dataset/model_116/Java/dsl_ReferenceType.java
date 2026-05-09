





import java.util.List;
import java.util.ArrayList;

public class dsl_ReferenceType  {

    private String squareBracketsBeta;
    private String primType;
    private String squareBracketsAlpha;





    private dsl_ClassOrInterfaceType dsl_classorinterfacetype;




    private dsl_Type dsl_type;


    public dsl_ReferenceType(
        String squareBracketsBeta,        String primType,        String squareBracketsAlpha    ) {
        this.squareBracketsBeta = squareBracketsBeta;
        this.primType = primType;
        this.squareBracketsAlpha = squareBracketsAlpha;
    }


    public String getSquarebracketsbeta() {
        return squareBracketsBeta;
    }

    public void setSquarebracketsbeta(String squareBracketsBeta) {
        this.squareBracketsBeta = squareBracketsBeta;
    }
    public String getPrimtype() {
        return primType;
    }

    public void setPrimtype(String primType) {
        this.primType = primType;
    }
    public String getSquarebracketsalpha() {
        return squareBracketsAlpha;
    }

    public void setSquarebracketsalpha(String squareBracketsAlpha) {
        this.squareBracketsAlpha = squareBracketsAlpha;
    }

    public dsl_ClassOrInterfaceType getDsl_classorinterfacetype() {
        return dsl_classorinterfacetype;
    }

    public void setDsl_classorinterfacetype(dsl_ClassOrInterfaceType dsl_classorinterfacetype) {
        this.dsl_classorinterfacetype = dsl_classorinterfacetype;
    }
    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }

}