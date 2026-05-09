





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_InvocationExpCS extends NamedExpCS {






    private List<essentialoclcs_NavigatingArgCS> essentialoclcs_navigatingargcss;




    private essentialoclcs_NavigatingArgCS essentialoclcs_navigatingargcs;


    public essentialoclcs_InvocationExpCS(
    ) {
        super(
        );
        this.essentialoclcs_navigatingargcss = new ArrayList<>();
    }

    public essentialoclcs_InvocationExpCS(
        ArrayList<essentialoclcs_NavigatingArgCS> essentialoclcs_navigatingargcss    ) {
        this.essentialoclcs_navigatingargcss = essentialoclcs_navigatingargcss;
    }


    public List<essentialoclcs_NavigatingArgCS> getEssentialoclcs_navigatingargcss() {
        return essentialoclcs_navigatingargcss;
    }

    public void addEssentialoclcs_navigatingargcs(Essentialoclcs_navigatingargcs essentialoclcs_navigatingargcs) {
        this.essentialoclcs_navigatingargcss.add(essentialoclcs_navigatingargcs);
    }
    public essentialoclcs_NavigatingArgCS getEssentialoclcs_navigatingargcs() {
        return essentialoclcs_navigatingargcs;
    }

    public void setEssentialoclcs_navigatingargcs(essentialoclcs_NavigatingArgCS essentialoclcs_navigatingargcs) {
        this.essentialoclcs_navigatingargcs = essentialoclcs_navigatingargcs;
    }

}