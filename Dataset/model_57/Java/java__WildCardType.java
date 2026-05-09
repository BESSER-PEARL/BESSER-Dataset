





import java.util.List;
import java.util.ArrayList;

public class java__WildCardType extends Type {

    private boolean upperBound;





    private java__TypeAccess java__typeaccess;


    public java__WildCardType(
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

    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }

}