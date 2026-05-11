





import java.util.List;
import java.util.ArrayList;

public class df_Port extends Vertex {

    private String name;
    private int numTokensConsumed;
    private int numTokensProduced;





    private df_Entity df_entity;




    private df_Entity df_entity;


    public df_Port(
        String name,        int numTokensConsumed,        int numTokensProduced    ) {
        super(
        );
        this.name = name;
        this.numTokensConsumed = numTokensConsumed;
        this.numTokensProduced = numTokensProduced;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumtokensconsumed() {
        return numTokensConsumed;
    }

    public void setNumtokensconsumed(int numTokensConsumed) {
        this.numTokensConsumed = numTokensConsumed;
    }
    public int getNumtokensproduced() {
        return numTokensProduced;
    }

    public void setNumtokensproduced(int numTokensProduced) {
        this.numTokensProduced = numTokensProduced;
    }

    public df_Entity getDf_entity() {
        return df_entity;
    }

    public void setDf_entity(df_Entity df_entity) {
        this.df_entity = df_entity;
    }
    public df_Entity getDf_entity() {
        return df_entity;
    }

    public void setDf_entity(df_Entity df_entity) {
        this.df_entity = df_entity;
    }

}