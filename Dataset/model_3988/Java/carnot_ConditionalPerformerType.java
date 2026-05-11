





import java.util.List;
import java.util.ArrayList;

public class carnot_ConditionalPerformerType extends IModelParticipant {

    private String isUser;
    private String dataPath;





    private carnot_DataType carnot_datatype;




    private carnot_ModelType carnot_modeltype;




    private carnot_ConditionalPerformerSymbolType carnot_conditionalperformersymboltype;




    private List<carnot_ConditionalPerformerSymbolType> carnot_conditionalperformersymboltypes;




    private carnot_DataType carnot_datatype;


    public carnot_ConditionalPerformerType(
        String isUser,        String dataPath    ) {
        super(
        );
        this.isUser = isUser;
        this.dataPath = dataPath;
        this.carnot_conditionalperformersymboltypes = new ArrayList<>();
    }

    public carnot_ConditionalPerformerType(
        String isUser,        String dataPath        ArrayList<carnot_ConditionalPerformerSymbolType> carnot_conditionalperformersymboltypes    ) {
        this.isUser = isUser;
        this.dataPath = dataPath;
        this.carnot_conditionalperformersymboltypes = carnot_conditionalperformersymboltypes;
    }

    public String getIsuser() {
        return isUser;
    }

    public void setIsuser(String isUser) {
        this.isUser = isUser;
    }
    public String getDatapath() {
        return dataPath;
    }

    public void setDatapath(String dataPath) {
        this.dataPath = dataPath;
    }

    public carnot_DataType getCarnot_datatype() {
        return carnot_datatype;
    }

    public void setCarnot_datatype(carnot_DataType carnot_datatype) {
        this.carnot_datatype = carnot_datatype;
    }
    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }
    public carnot_ConditionalPerformerSymbolType getCarnot_conditionalperformersymboltype() {
        return carnot_conditionalperformersymboltype;
    }

    public void setCarnot_conditionalperformersymboltype(carnot_ConditionalPerformerSymbolType carnot_conditionalperformersymboltype) {
        this.carnot_conditionalperformersymboltype = carnot_conditionalperformersymboltype;
    }
    public List<carnot_ConditionalPerformerSymbolType> getCarnot_conditionalperformersymboltypes() {
        return carnot_conditionalperformersymboltypes;
    }

    public void addCarnot_conditionalperformersymboltype(Carnot_conditionalperformersymboltype carnot_conditionalperformersymboltype) {
        this.carnot_conditionalperformersymboltypes.add(carnot_conditionalperformersymboltype);
    }
    public carnot_DataType getCarnot_datatype() {
        return carnot_datatype;
    }

    public void setCarnot_datatype(carnot_DataType carnot_datatype) {
        this.carnot_datatype = carnot_datatype;
    }

}