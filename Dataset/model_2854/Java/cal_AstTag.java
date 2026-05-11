





import java.util.List;
import java.util.ArrayList;

public class cal_AstTag  {

    private String identifiers;





    private cal_AstInequality cal_astinequality;




    private cal_AstAction cal_astaction;


    public cal_AstTag(
        String identifiers    ) {
        this.identifiers = identifiers;
    }


    public String getIdentifiers() {
        return identifiers;
    }

    public void setIdentifiers(String identifiers) {
        this.identifiers = identifiers;
    }

    public cal_AstInequality getCal_astinequality() {
        return cal_astinequality;
    }

    public void setCal_astinequality(cal_AstInequality cal_astinequality) {
        this.cal_astinequality = cal_astinequality;
    }
    public cal_AstAction getCal_astaction() {
        return cal_astaction;
    }

    public void setCal_astaction(cal_AstAction cal_astaction) {
        this.cal_astaction = cal_astaction;
    }

}