





import java.util.List;
import java.util.ArrayList;

public class BinaryCalculator_BinaryCalculator  {

    private String description;





    private BinaryCalculator_BitSeq binarycalculator_bitseq;




    private BinaryCalculator_Value binarycalculator_value;




    private BinaryCalculator_Model binarycalculator_model;


    public BinaryCalculator_BinaryCalculator(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public BinaryCalculator_BitSeq getBinarycalculator_bitseq() {
        return binarycalculator_bitseq;
    }

    public void setBinarycalculator_bitseq(BinaryCalculator_BitSeq binarycalculator_bitseq) {
        this.binarycalculator_bitseq = binarycalculator_bitseq;
    }
    public BinaryCalculator_Value getBinarycalculator_value() {
        return binarycalculator_value;
    }

    public void setBinarycalculator_value(BinaryCalculator_Value binarycalculator_value) {
        this.binarycalculator_value = binarycalculator_value;
    }
    public BinaryCalculator_Model getBinarycalculator_model() {
        return binarycalculator_model;
    }

    public void setBinarycalculator_model(BinaryCalculator_Model binarycalculator_model) {
        this.binarycalculator_model = binarycalculator_model;
    }

}