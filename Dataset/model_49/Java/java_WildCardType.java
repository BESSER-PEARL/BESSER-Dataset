





import java.util.List;
import java.util.ArrayList;

public class java_WildCardType extends Type {

    private boolean upperBound;





    private java_TypeAccess java_typeaccess;


    public java_WildCardType(
        boolean upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
    }


    public boolean getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(boolean upperBound) {
        this.upperBound = upperBound;
    }

    public java_TypeAccess getJava_typeaccess() {
        return java_typeaccess;
    }

    public void setJava_typeaccess(java_TypeAccess java_typeaccess) {
        this.java_typeaccess = java_typeaccess;
    }

}