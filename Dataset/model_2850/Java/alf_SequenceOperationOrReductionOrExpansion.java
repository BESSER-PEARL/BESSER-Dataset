





import java.util.List;
import java.util.ArrayList;

public class alf_SequenceOperationOrReductionOrExpansion  {

    private boolean isOrdered;
    private String id;
    private boolean isReduce;





    private alf_TemplateBinding alf_templatebinding;




    private alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index alf_feature_or_sequenceoperationorreductionorexpansion_or_index;




    private alf_Name alf_name;


    public alf_SequenceOperationOrReductionOrExpansion(
        boolean isOrdered,        String id,        boolean isReduce    ) {
        this.isOrdered = isOrdered;
        this.id = id;
        this.isReduce = isReduce;
    }


    public boolean getIsordered() {
        return isOrdered;
    }

    public void setIsordered(boolean isOrdered) {
        this.isOrdered = isOrdered;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getIsreduce() {
        return isReduce;
    }

    public void setIsreduce(boolean isReduce) {
        this.isReduce = isReduce;
    }

    public alf_TemplateBinding getAlf_templatebinding() {
        return alf_templatebinding;
    }

    public void setAlf_templatebinding(alf_TemplateBinding alf_templatebinding) {
        this.alf_templatebinding = alf_templatebinding;
    }
    public alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index getAlf_feature_or_sequenceoperationorreductionorexpansion_or_index() {
        return alf_feature_or_sequenceoperationorreductionorexpansion_or_index;
    }

    public void setAlf_feature_or_sequenceoperationorreductionorexpansion_or_index(alf_Feature_Or_SequenceOperationOrReductionOrExpansion_Or_Index alf_feature_or_sequenceoperationorreductionorexpansion_or_index) {
        this.alf_feature_or_sequenceoperationorreductionorexpansion_or_index = alf_feature_or_sequenceoperationorreductionorexpansion_or_index;
    }
    public alf_Name getAlf_name() {
        return alf_name;
    }

    public void setAlf_name(alf_Name alf_name) {
        this.alf_name = alf_name;
    }

}