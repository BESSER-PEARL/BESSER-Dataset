





import java.util.List;
import java.util.ArrayList;

public class query_XMLSerializeFunction extends ValueExpressionFunction {

    private String contentOption;
    private String declarationOption;
    private String serializeVersion;





    private query_XMLSerializeFunctionTarget query_xmlserializefunctiontarget;




    private query_XMLSerializeFunctionTarget query_xmlserializefunctiontarget;


    public query_XMLSerializeFunction(
        String contentOption,        String declarationOption,        String serializeVersion    ) {
        super(
        );
        this.contentOption = contentOption;
        this.declarationOption = declarationOption;
        this.serializeVersion = serializeVersion;
    }


    public String getContentoption() {
        return contentOption;
    }

    public void setContentoption(String contentOption) {
        this.contentOption = contentOption;
    }
    public String getDeclarationoption() {
        return declarationOption;
    }

    public void setDeclarationoption(String declarationOption) {
        this.declarationOption = declarationOption;
    }
    public String getSerializeversion() {
        return serializeVersion;
    }

    public void setSerializeversion(String serializeVersion) {
        this.serializeVersion = serializeVersion;
    }

    public query_XMLSerializeFunctionTarget getQuery_xmlserializefunctiontarget() {
        return query_xmlserializefunctiontarget;
    }

    public void setQuery_xmlserializefunctiontarget(query_XMLSerializeFunctionTarget query_xmlserializefunctiontarget) {
        this.query_xmlserializefunctiontarget = query_xmlserializefunctiontarget;
    }
    public query_XMLSerializeFunctionTarget getQuery_xmlserializefunctiontarget() {
        return query_xmlserializefunctiontarget;
    }

    public void setQuery_xmlserializefunctiontarget(query_XMLSerializeFunctionTarget query_xmlserializefunctiontarget) {
        this.query_xmlserializefunctiontarget = query_xmlserializefunctiontarget;
    }

}