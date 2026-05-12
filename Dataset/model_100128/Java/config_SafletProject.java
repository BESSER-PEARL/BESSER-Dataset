





import java.util.List;
import java.util.ArrayList;

public class config_SafletProject  {






    private db_config_Saflet db_config_saflet;




    private db_config_Prompt db_config_prompt;


    public config_SafletProject(
    ) {
    }



    public db_config_Saflet getDb_config_saflet() {
        return db_config_saflet;
    }

    public void setDb_config_saflet(db_config_Saflet db_config_saflet) {
        this.db_config_saflet = db_config_saflet;
    }
    public db_config_Prompt getDb_config_prompt() {
        return db_config_prompt;
    }

    public void setDb_config_prompt(db_config_Prompt db_config_prompt) {
        this.db_config_prompt = db_config_prompt;
    }

}