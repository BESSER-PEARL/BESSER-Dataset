





import java.util.List;
import java.util.ArrayList;

public class Graphql_EnumValue  {

    private String value;
    private String number;





    private Graphql_Enum graphql_enum;


    public Graphql_EnumValue(
        String value,        String number    ) {
        this.value = value;
        this.number = number;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public Graphql_Enum getGraphql_enum() {
        return graphql_enum;
    }

    public void setGraphql_enum(Graphql_Enum graphql_enum) {
        this.graphql_enum = graphql_enum;
    }

}