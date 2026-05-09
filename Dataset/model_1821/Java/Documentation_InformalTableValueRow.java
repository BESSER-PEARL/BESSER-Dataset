





import java.util.List;
import java.util.ArrayList;

public class Documentation_InformalTableValueRow  {






    private Documentation_InformalTableValue documentation_informaltablevalue;




    private Documentation_InformalTableValue documentation_informaltablevalue;




    private List<Documentation_TextualValue> documentation_textualvalues;


    public Documentation_InformalTableValueRow(
    ) {
        this.documentation_textualvalues = new ArrayList<>();
    }

    public Documentation_InformalTableValueRow(
        ArrayList<Documentation_TextualValue> documentation_textualvalues    ) {
        this.documentation_textualvalues = documentation_textualvalues;
    }


    public Documentation_InformalTableValue getDocumentation_informaltablevalue() {
        return documentation_informaltablevalue;
    }

    public void setDocumentation_informaltablevalue(Documentation_InformalTableValue documentation_informaltablevalue) {
        this.documentation_informaltablevalue = documentation_informaltablevalue;
    }
    public Documentation_InformalTableValue getDocumentation_informaltablevalue() {
        return documentation_informaltablevalue;
    }

    public void setDocumentation_informaltablevalue(Documentation_InformalTableValue documentation_informaltablevalue) {
        this.documentation_informaltablevalue = documentation_informaltablevalue;
    }
    public List<Documentation_TextualValue> getDocumentation_textualvalues() {
        return documentation_textualvalues;
    }

    public void addDocumentation_textualvalue(Documentation_textualvalue documentation_textualvalue) {
        this.documentation_textualvalues.add(documentation_textualvalue);
    }

}