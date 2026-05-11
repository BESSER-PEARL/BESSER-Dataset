





import java.util.List;
import java.util.ArrayList;

public class carnot_ConditionalPerformerType extends IModelParticipant {

    private String dataPath;
    private String isUser;





    private carnot_ConditionalPerformerSymbolType carnot_conditionalperformersymboltype;




    private carnot_DataType carnot_datatype;




    private carnot_DataType carnot_datatype;




    private List<carnot_ConditionalPerformerSymbolType> carnot_conditionalperformersymboltypes;




    private carnot_ModelType carnot_modeltype;


    public carnot_ConditionalPerformerType(
        String dataPath,        String isUser    ) {
        super(
        );
        this.dataPath = dataPath;
        this.isUser = isUser;
        this.carnot_conditionalperformersymboltypes = new ArrayList<>();
    }

    public carnot_ConditionalPerformerType(
        String dataPath,        String isUser        ArrayList<carnot_ConditionalPerformerSymbolType> carnot_conditionalperformersymboltypes    ) {
        this.dataPath = dataPath;
        this.isUser = isUser;
        this.carnot_conditionalperformersymboltypes = carnot_conditionalperformersymboltypes;
    }

    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
    }
    public String getIsuser() {
        return isUser;
    }

    public void setIsuser(String isUser) {
        this.isUser = isUser;
    }

    public carnot_ConditionalPerformerSymbolType getCarnot_conditionalperformersymboltype() {
        return carnot_conditionalperformersymboltype;
    }

    public void setCarnot_conditionalperformersymboltype(carnot_ConditionalPerformerSymbolType carnot_conditionalperformersymboltype) {
        this.carnot_conditionalperformersymboltype = carnot_conditionalperformersymboltype;
    }
    public carnot_DataType getCarnot_datatype() {
        return carnot_datatype;
    }

    public void setCarnot_datatype(carnot_DataType carnot_datatype) {
        this.carnot_datatype = carnot_datatype;
    }
    public carnot_DataType getCarnot_datatype() {
        return carnot_datatype;
    }

    public void setCarnot_datatype(carnot_DataType carnot_datatype) {
        this.carnot_datatype = carnot_datatype;
    }
    public List<carnot_ConditionalPerformerSymbolType> getCarnot_conditionalperformersymboltypes() {
        return carnot_conditionalperformersymboltypes;
    }

    public void addCarnot_conditionalperformersymboltype(Carnot_conditionalperformersymboltype carnot_conditionalperformersymboltype) {
        this.carnot_conditionalperformersymboltypes.add(carnot_conditionalperformersymboltype);
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}