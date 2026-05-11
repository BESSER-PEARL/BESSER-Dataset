





import java.util.List;
import java.util.ArrayList;

public class avm_Value extends ValueNode {

    private String DimensionType;
    private String Dimensions;
    private String Unit;
    private String DataType;





    private avm_ComponentPrimitivePropertyInstance avm_componentprimitivepropertyinstance;




    private avm_PrimitiveProperty avm_primitiveproperty;




    private avm_DomainModelMetric avm_domainmodelmetric;




    private avm_TestBenchValueBase avm_testbenchvaluebase;




    private List<avm_DataSource> avm_datasources;


    public avm_Value(
        String DimensionType,        String Dimensions,        String Unit,        String DataType    ) {
        super(
        );
        this.DimensionType = DimensionType;
        this.Dimensions = Dimensions;
        this.Unit = Unit;
        this.DataType = DataType;
        this.avm_datasources = new ArrayList<>();
    }

    public avm_Value(
        String DimensionType,        String Dimensions,        String Unit,        String DataType        ArrayList<avm_DataSource> avm_datasources    ) {
        this.DimensionType = DimensionType;
        this.Dimensions = Dimensions;
        this.Unit = Unit;
        this.DataType = DataType;
        this.avm_datasources = avm_datasources;
    }

    public String getDimensiontype() {
        return DimensionType;
    }

    public void setDimensiontype(String DimensionType) {
        this.DimensionType = DimensionType;
    }
    public String getDimensions() {
        return Dimensions;
    }

    public void setDimensions(String Dimensions) {
        this.Dimensions = Dimensions;
    }
    public String getUnit() {
        return Unit;
    }

    public void setUnit(String Unit) {
        this.Unit = Unit;
    }
    public String getDatatype() {
        return DataType;
    }

    public void setDatatype(String DataType) {
        this.DataType = DataType;
    }

    public avm_ComponentPrimitivePropertyInstance getAvm_componentprimitivepropertyinstance() {
        return avm_componentprimitivepropertyinstance;
    }

    public void setAvm_componentprimitivepropertyinstance(avm_ComponentPrimitivePropertyInstance avm_componentprimitivepropertyinstance) {
        this.avm_componentprimitivepropertyinstance = avm_componentprimitivepropertyinstance;
    }
    public avm_PrimitiveProperty getAvm_primitiveproperty() {
        return avm_primitiveproperty;
    }

    public void setAvm_primitiveproperty(avm_PrimitiveProperty avm_primitiveproperty) {
        this.avm_primitiveproperty = avm_primitiveproperty;
    }
    public avm_DomainModelMetric getAvm_domainmodelmetric() {
        return avm_domainmodelmetric;
    }

    public void setAvm_domainmodelmetric(avm_DomainModelMetric avm_domainmodelmetric) {
        this.avm_domainmodelmetric = avm_domainmodelmetric;
    }
    public avm_TestBenchValueBase getAvm_testbenchvaluebase() {
        return avm_testbenchvaluebase;
    }

    public void setAvm_testbenchvaluebase(avm_TestBenchValueBase avm_testbenchvaluebase) {
        this.avm_testbenchvaluebase = avm_testbenchvaluebase;
    }
    public List<avm_DataSource> getAvm_datasources() {
        return avm_datasources;
    }

    public void addAvm_datasource(Avm_datasource avm_datasource) {
        this.avm_datasources.add(avm_datasource);
    }

}