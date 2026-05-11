





import java.util.List;
import java.util.ArrayList;

public class langage_while_Command  {

    private String nop;





    private langage_while_Commands langage_while_commands;




    private langage_while_Ifconfort langage_while_ifconfort;


    public langage_while_Command(
        String nop    ) {
        this.nop = nop;
    }


    public String getNop() {
        return nop;
    }

    public void setNop(String nop) {
        this.nop = nop;
    }

    public langage_while_Commands getLangage_while_commands() {
        return langage_while_commands;
    }

    public void setLangage_while_commands(langage_while_Commands langage_while_commands) {
        this.langage_while_commands = langage_while_commands;
    }
    public langage_while_Ifconfort getLangage_while_ifconfort() {
        return langage_while_ifconfort;
    }

    public void setLangage_while_ifconfort(langage_while_Ifconfort langage_while_ifconfort) {
        this.langage_while_ifconfort = langage_while_ifconfort;
    }

}