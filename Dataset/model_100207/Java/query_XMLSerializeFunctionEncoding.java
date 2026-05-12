





import java.util.List;
import java.util.ArrayList;

public class query_XMLSerializeFunctionEncoding extends SQLQueryObject {

    private String encodingName;





    private query_XMLSerializeFunction query_xmlserializefunction;


    public query_XMLSerializeFunctionEncoding(
        String encodingName    ) {
        super(
        );
        this.encodingName = encodingName;
    }


    public String getEncodingname() {
        return encodingName;
    }

    public void setEncodingname(String encodingName) {
        this.encodingName = encodingName;
    }

    public query_XMLSerializeFunction getQuery_xmlserializefunction() {
        return query_xmlserializefunction;
    }

    public void setQuery_xmlserializefunction(query_XMLSerializeFunction query_xmlserializefunction) {
        this.query_xmlserializefunction = query_xmlserializefunction;
    }

}