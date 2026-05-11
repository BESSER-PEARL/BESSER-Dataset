





import java.util.List;
import java.util.ArrayList;

public class carnot_TextSymbolType extends INodeSymbol {

    private String text;





    private carnot_ISymbolContainer carnot_isymbolcontainer;


    public carnot_TextSymbolType(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public carnot_ISymbolContainer getCarnot_isymbolcontainer() {
        return carnot_isymbolcontainer;
    }

    public void setCarnot_isymbolcontainer(carnot_ISymbolContainer carnot_isymbolcontainer) {
        this.carnot_isymbolcontainer = carnot_isymbolcontainer;
    }

}