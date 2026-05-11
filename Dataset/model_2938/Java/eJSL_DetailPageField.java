





import java.util.List;
import java.util.ArrayList;

public class eJSL_DetailPageField  {






    private eJSL_Attribute ejsl_attribute;




    private eJSL_HTMLTypes ejsl_htmltypes;




    private eJSL_DetailsPage ejsl_detailspage;




    private List<eJSL_KeyValuePair> ejsl_keyvaluepairs;




    private List<eJSL_KeyValuePair> ejsl_keyvaluepairs;


    public eJSL_DetailPageField(
    ) {
        this.ejsl_keyvaluepairs = new ArrayList<>();
        this.ejsl_keyvaluepairs = new ArrayList<>();
    }

    public eJSL_DetailPageField(
        ArrayList<eJSL_KeyValuePair> ejsl_keyvaluepairs,        ArrayList<eJSL_KeyValuePair> ejsl_keyvaluepairs    ) {
        this.ejsl_keyvaluepairs = ejsl_keyvaluepairs;
        this.ejsl_keyvaluepairs = ejsl_keyvaluepairs;
    }


    public eJSL_Attribute getEjsl_attribute() {
        return ejsl_attribute;
    }

    public void setEjsl_attribute(eJSL_Attribute ejsl_attribute) {
        this.ejsl_attribute = ejsl_attribute;
    }
    public eJSL_HTMLTypes getEjsl_htmltypes() {
        return ejsl_htmltypes;
    }

    public void setEjsl_htmltypes(eJSL_HTMLTypes ejsl_htmltypes) {
        this.ejsl_htmltypes = ejsl_htmltypes;
    }
    public eJSL_DetailsPage getEjsl_detailspage() {
        return ejsl_detailspage;
    }

    public void setEjsl_detailspage(eJSL_DetailsPage ejsl_detailspage) {
        this.ejsl_detailspage = ejsl_detailspage;
    }
    public List<eJSL_KeyValuePair> getEjsl_keyvaluepairs() {
        return ejsl_keyvaluepairs;
    }

    public void addEjsl_keyvaluepair(Ejsl_keyvaluepair ejsl_keyvaluepair) {
        this.ejsl_keyvaluepairs.add(ejsl_keyvaluepair);
    }
    public List<eJSL_KeyValuePair> getEjsl_keyvaluepairs() {
        return ejsl_keyvaluepairs;
    }

    public void addEjsl_keyvaluepair(Ejsl_keyvaluepair ejsl_keyvaluepair) {
        this.ejsl_keyvaluepairs.add(ejsl_keyvaluepair);
    }

}