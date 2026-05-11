





import java.util.List;
import java.util.ArrayList;

public class eJSL_Component extends Extension {






    private List<eJSL_Section> ejsl_sections;




    private List<eJSL_ParameterGroup> ejsl_parametergroups;


    public eJSL_Component(
    ) {
        super(
        );
        this.ejsl_sections = new ArrayList<>();
        this.ejsl_parametergroups = new ArrayList<>();
    }

    public eJSL_Component(
        ArrayList<eJSL_Section> ejsl_sections,        ArrayList<eJSL_ParameterGroup> ejsl_parametergroups    ) {
        this.ejsl_sections = ejsl_sections;
        this.ejsl_parametergroups = ejsl_parametergroups;
    }


    public List<eJSL_Section> getEjsl_sections() {
        return ejsl_sections;
    }

    public void addEjsl_section(Ejsl_section ejsl_section) {
        this.ejsl_sections.add(ejsl_section);
    }
    public List<eJSL_ParameterGroup> getEjsl_parametergroups() {
        return ejsl_parametergroups;
    }

    public void addEjsl_parametergroup(Ejsl_parametergroup ejsl_parametergroup) {
        this.ejsl_parametergroups.add(ejsl_parametergroup);
    }

}