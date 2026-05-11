





import java.util.List;
import java.util.ArrayList;

public class cal_AstTag  {

    private String identifiers;





    private cal_AstAction cal_astaction;




    private cal_AstTransition cal_asttransition;


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

    public cal_AstAction getCal_astaction() {
        return cal_astaction;
    }

    public void setCal_astaction(cal_AstAction cal_astaction) {
        this.cal_astaction = cal_astaction;
    }
    public cal_AstTransition getCal_asttransition() {
        return cal_asttransition;
    }

    public void setCal_asttransition(cal_AstTransition cal_asttransition) {
        this.cal_asttransition = cal_asttransition;
    }

}