





import java.util.List;
import java.util.ArrayList;

public class Commutator  {

    private None builder;
    private String commutatorTrain;



    public Commutator(
        None builder,        String commutatorTrain    ) {
        this.builder = builder;
        this.commutatorTrain = commutatorTrain;
    }


    public None getBuilder() {
        return builder;
    }

    public void setBuilder(None builder) {
        this.builder = builder;
    }
    public String getCommutatortrain() {
        return commutatorTrain;
    }

    public void setCommutatortrain(String commutatorTrain) {
        this.commutatorTrain = commutatorTrain;
    }


}