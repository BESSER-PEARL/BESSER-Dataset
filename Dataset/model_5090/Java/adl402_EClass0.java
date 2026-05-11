





import java.util.List;
import java.util.ArrayList;

public class adl402_EClass0  {

    private String EAttribute0;





    private List<adl402_EClass0> adl402_eclass0s;


    public adl402_EClass0(
        String EAttribute0    ) {
        this.EAttribute0 = EAttribute0;
        this.adl402_eclass0s = new ArrayList<>();
    }

    public adl402_EClass0(
        String EAttribute0        ArrayList<adl402_EClass0> adl402_eclass0s    ) {
        this.EAttribute0 = EAttribute0;
        this.adl402_eclass0s = adl402_eclass0s;
    }

    public String getEattribute0() {
        return EAttribute0;
    }

    public void setEattribute0(String EAttribute0) {
        this.EAttribute0 = EAttribute0;
    }

    public List<adl402_EClass0> getAdl402_eclass0s() {
        return adl402_eclass0s;
    }

    public void addAdl402_eclass0(Adl402_eclass0 adl402_eclass0) {
        this.adl402_eclass0s.add(adl402_eclass0);
    }

}