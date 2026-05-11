





import java.util.List;
import java.util.ArrayList;

public class coCoMM_CrossModelConstraint  {






    private List<coCoMM_CMConstraintExpression> cocomm_cmconstraintexpressions;




    private coCoMM_CoCo cocomm_coco;


    public coCoMM_CrossModelConstraint(
    ) {
        this.cocomm_cmconstraintexpressions = new ArrayList<>();
    }

    public coCoMM_CrossModelConstraint(
        ArrayList<coCoMM_CMConstraintExpression> cocomm_cmconstraintexpressions    ) {
        this.cocomm_cmconstraintexpressions = cocomm_cmconstraintexpressions;
    }


    public List<coCoMM_CMConstraintExpression> getCocomm_cmconstraintexpressions() {
        return cocomm_cmconstraintexpressions;
    }

    public void addCocomm_cmconstraintexpression(Cocomm_cmconstraintexpression cocomm_cmconstraintexpression) {
        this.cocomm_cmconstraintexpressions.add(cocomm_cmconstraintexpression);
    }
    public coCoMM_CoCo getCocomm_coco() {
        return cocomm_coco;
    }

    public void setCocomm_coco(coCoMM_CoCo cocomm_coco) {
        this.cocomm_coco = cocomm_coco;
    }

}