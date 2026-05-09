





import java.util.List;
import java.util.ArrayList;

public class javaMM_WildCardType extends Type {

    private String upperBound;





    private javaMM_TypeAccess javamm_typeaccess;


    public javaMM_WildCardType(
        String upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }

    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }

}