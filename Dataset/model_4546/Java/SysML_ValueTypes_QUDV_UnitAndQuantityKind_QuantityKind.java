





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind  {

    private String symbol;
    private String definitionURI;
    private String description;
    private String name;



    public SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind(
        String symbol,        String definitionURI,        String description,        String name    ) {
        this.symbol = symbol;
        this.definitionURI = definitionURI;
        this.description = description;
        this.name = name;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getDefinitionuri() {
        return definitionURI;
    }

    public void setDefinitionuri(String definitionURI) {
        this.definitionURI = definitionURI;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}