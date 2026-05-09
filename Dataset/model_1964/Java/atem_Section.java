





import java.util.List;
import java.util.ArrayList;

public class atem_Section extends AbstractComponent, PrefaceElementType, SectionElementType {

    private String name;





    private atem_SectionFragment atem_sectionfragment;


    public atem_Section(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public atem_SectionFragment getAtem_sectionfragment() {
        return atem_sectionfragment;
    }

    public void setAtem_sectionfragment(atem_SectionFragment atem_sectionfragment) {
        this.atem_sectionfragment = atem_sectionfragment;
    }

}