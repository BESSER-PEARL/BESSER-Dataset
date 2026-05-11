





import java.util.List;
import java.util.ArrayList;

public class mid_ExtendibleElementConstraint  {

    private String implementation;
    private String language;





    private mid_ExtendibleElement mid_extendibleelement;


    public mid_ExtendibleElementConstraint(
        String implementation,        String language    ) {
        this.implementation = implementation;
        this.language = language;
    }


    public String getImplementation() {
        return implementation;
    }

    public void setImplementation(String implementation) {
        this.implementation = implementation;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public mid_ExtendibleElement getMid_extendibleelement() {
        return mid_extendibleelement;
    }

    public void setMid_extendibleelement(mid_ExtendibleElement mid_extendibleelement) {
        this.mid_extendibleelement = mid_extendibleelement;
    }

}