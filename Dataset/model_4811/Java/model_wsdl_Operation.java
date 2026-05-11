





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Operation extends wsdl_IOperation, wsdl_ExtensibleElement {

    private boolean undefined;
    private String name;
    private String style;





    private List<Part> parts;


    public model_wsdl_Operation(
        boolean undefined,        String name,        String style    ) {
        super(
        );
        this.undefined = undefined;
        this.name = name;
        this.style = style;
        this.parts = new ArrayList<>();
    }

    public model_wsdl_Operation(
        boolean undefined,        String name,        String style        ArrayList<Part> parts    ) {
        this.undefined = undefined;
        this.name = name;
        this.style = style;
        this.parts = parts;
    }

    public boolean getUndefined() {
        return undefined;
    }

    public void setUndefined(boolean undefined) {
        this.undefined = undefined;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public List<Part> getParts() {
        return parts;
    }

    public void addPart(Part part) {
        this.parts.add(part);
    }

}