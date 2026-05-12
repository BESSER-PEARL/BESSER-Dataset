





import java.util.List;
import java.util.ArrayList;

public class Documentation_ItemizedListValue extends ParagraphValue {






    private List<Documentation_ItemizedListValueItem> documentation_itemizedlistvalueitems;


    public Documentation_ItemizedListValue(
    ) {
        super(
        );
        this.documentation_itemizedlistvalueitems = new ArrayList<>();
    }

    public Documentation_ItemizedListValue(
        ArrayList<Documentation_ItemizedListValueItem> documentation_itemizedlistvalueitems    ) {
        this.documentation_itemizedlistvalueitems = documentation_itemizedlistvalueitems;
    }


    public List<Documentation_ItemizedListValueItem> getDocumentation_itemizedlistvalueitems() {
        return documentation_itemizedlistvalueitems;
    }

    public void addDocumentation_itemizedlistvalueitem(Documentation_itemizedlistvalueitem documentation_itemizedlistvalueitem) {
        this.documentation_itemizedlistvalueitems.add(documentation_itemizedlistvalueitem);
    }

}