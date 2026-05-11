





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_Method  {

    private String body;
    private String name;





    private SQL2003_V2_StructuredType sql2003_v2_structuredtype;




    private SQL2003_V2_Method sql2003_v2_method;




    private SQL2003_V2_StructuredType sql2003_v2_structuredtype;




    private SQL2003_V2_DataType sql2003_v2_datatype;


    public SQL2003_V2_Method(
        String body,        String name    ) {
        this.body = body;
        this.name = name;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SQL2003_V2_StructuredType getSql2003_v2_structuredtype() {
        return sql2003_v2_structuredtype;
    }

    public void setSql2003_v2_structuredtype(SQL2003_V2_StructuredType sql2003_v2_structuredtype) {
        this.sql2003_v2_structuredtype = sql2003_v2_structuredtype;
    }
    public SQL2003_V2_Method getSql2003_v2_method() {
        return sql2003_v2_method;
    }

    public void setSql2003_v2_method(SQL2003_V2_Method sql2003_v2_method) {
        this.sql2003_v2_method = sql2003_v2_method;
    }
    public SQL2003_V2_StructuredType getSql2003_v2_structuredtype() {
        return sql2003_v2_structuredtype;
    }

    public void setSql2003_v2_structuredtype(SQL2003_V2_StructuredType sql2003_v2_structuredtype) {
        this.sql2003_v2_structuredtype = sql2003_v2_structuredtype;
    }
    public SQL2003_V2_DataType getSql2003_v2_datatype() {
        return sql2003_v2_datatype;
    }

    public void setSql2003_v2_datatype(SQL2003_V2_DataType sql2003_v2_datatype) {
        this.sql2003_v2_datatype = sql2003_v2_datatype;
    }

}