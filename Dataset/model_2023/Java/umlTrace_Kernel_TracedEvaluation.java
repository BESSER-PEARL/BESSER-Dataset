





import java.util.List;
import java.util.ArrayList;

public class umlTrace_Kernel_TracedEvaluation extends TracedSemanticVisitor {






    private List<Evaluation_specification_Evaluation_Value> evaluation_specification_evaluation_values;




    private List<Evaluation_locus_Evaluation_Value> evaluation_locus_evaluation_values;


    public umlTrace_Kernel_TracedEvaluation(
    ) {
        super(
        );
        this.evaluation_specification_evaluation_values = new ArrayList<>();
        this.evaluation_locus_evaluation_values = new ArrayList<>();
    }

    public umlTrace_Kernel_TracedEvaluation(
        ArrayList<Evaluation_specification_Evaluation_Value> evaluation_specification_evaluation_values,        ArrayList<Evaluation_locus_Evaluation_Value> evaluation_locus_evaluation_values    ) {
        this.evaluation_specification_evaluation_values = evaluation_specification_evaluation_values;
        this.evaluation_locus_evaluation_values = evaluation_locus_evaluation_values;
    }


    public List<Evaluation_specification_Evaluation_Value> getEvaluation_specification_evaluation_values() {
        return evaluation_specification_evaluation_values;
    }

    public void addEvaluation_specification_evaluation_value(Evaluation_specification_evaluation_value evaluation_specification_evaluation_value) {
        this.evaluation_specification_evaluation_values.add(evaluation_specification_evaluation_value);
    }
    public List<Evaluation_locus_Evaluation_Value> getEvaluation_locus_evaluation_values() {
        return evaluation_locus_evaluation_values;
    }

    public void addEvaluation_locus_evaluation_value(Evaluation_locus_evaluation_value evaluation_locus_evaluation_value) {
        this.evaluation_locus_evaluation_values.add(evaluation_locus_evaluation_value);
    }

}