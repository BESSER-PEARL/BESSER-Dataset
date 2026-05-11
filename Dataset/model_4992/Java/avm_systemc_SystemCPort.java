





import java.util.List;
import java.util.ArrayList;

public class avm_systemc_SystemCPort extends DomainModelPort {

    private String DataType;
    private String Function;
    private String Directionality;
    private String DataTypeDimension;



    public avm_systemc_SystemCPort(
        String DataType,        String Function,        String Directionality,        String DataTypeDimension    ) {
        super(
        );
        this.DataType = DataType;
        this.Function = Function;
        this.Directionality = Directionality;
        this.DataTypeDimension = DataTypeDimension;
    }


    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }
    public String getFunction() {
        return Function;
    }

    public void setFunction(String Function) {
        this.Function = Function;
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


}