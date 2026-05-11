





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind  {

    private String name;
    private String symbol;
    private String description;
    private String definitionURI;



    public SysML_ValueTypes_QUDV_UnitAndQuantityKind_QuantityKind(
        String name,        String symbol,        String description,        String definitionURI    ) {
        this.name = name;
        this.symbol = symbol;
        this.description = description;
        this.definitionURI = definitionURI;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDefinitionuri() {
        return definitionURI;
    }

    public void setDefinitionuri(String definitionURI) {
        this.definitionURI = definitionURI;
    }


}