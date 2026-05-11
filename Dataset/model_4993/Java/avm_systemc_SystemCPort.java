





import java.util.List;
import java.util.ArrayList;

public class avm_systemc_SystemCPort extends DomainModelPort {

    private String DataType;
    private String Directionality;
    private String DataTypeDimension;
    private String Function;



    public avm_systemc_SystemCPort(
        String DataType,        String Directionality,        String DataTypeDimension,        String Function    ) {
        super(
        );
        this.DataType = DataType;
        this.Directionality = Directionality;
        this.DataTypeDimension = DataTypeDimension;
        this.Function = Function;
    }


    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }
    public String getDirectionality() {
        return Directionality;
    }

    public void setDirectionality(String Directionality) {
        this.Directionality = Directionality;
    }
    public String getDatatypedimension() {
        return DataTypeDimension;
    }

    public void setDatatypedimension(String DataTypeDimension) {
        this.DataTypeDimension = DataTypeDimension;
    }
    public String getFunction() {
        return Function;
    }

    public void setFunction(String Function) {
        this.Function = Function;
    }


}