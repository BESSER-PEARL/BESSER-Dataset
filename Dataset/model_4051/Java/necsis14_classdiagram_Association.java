





import java.util.List;
import java.util.ArrayList;

public class necsis14_classdiagram_Association extends NamedElement {

    private int lowerBound;
    private int upperBound;





    private necsis14_classdiagram_Class necsis14_classdiagram_class;




    private necsis14_classdiagram_Class necsis14_classdiagram_class;


    public necsis14_classdiagram_Association(
        int lowerBound,        int upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public necsis14_classdiagram_Class getNecsis14_classdiagram_class() {
        return necsis14_classdiagram_class;
    }

    public void setNecsis14_classdiagram_class(necsis14_classdiagram_Class necsis14_classdiagram_class) {
        this.necsis14_classdiagram_class = necsis14_classdiagram_class;
    }
    public necsis14_classdiagram_Class getNecsis14_classdiagram_class() {
        return necsis14_classdiagram_class;
    }

    public void setNecsis14_classdiagram_class(necsis14_classdiagram_Class necsis14_classdiagram_class) {
        this.necsis14_classdiagram_class = necsis14_classdiagram_class;
    }

}