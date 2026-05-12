





import java.util.List;
import java.util.ArrayList;

public class Commutator  {

    private String commutatorTrain;
    private None builder;



    public Commutator(
        String commutatorTrain,        None builder    ) {
        this.commutatorTrain = commutatorTrain;
        this.builder = builder;
    }


    public String getCommutatortrain() {
        return commutatorTrain;
    }

    public void setCommutatortrain(String commutatorTrain) {
        this.commutatorTrain = commutatorTrain;
    }
    public None getBuilder() {
        return builder;
    }

    public void setBuilder(None builder) {
        this.builder = builder;
    }


}