





import java.util.List;
import java.util.ArrayList;

public class connect_four_gui_GUIPlayer  {

    private String board;
    private String m_name;
    private None gpGUI;



    public connect_four_gui_GUIPlayer(
        String board,        String m_name,        None gpGUI    ) {
        this.board = board;
        this.m_name = m_name;
        this.gpGUI = gpGUI;
    }


    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public String getM_name() {
        return m_name;
    }

    public void setM_name(String m_name) {
        this.m_name = m_name;
    }
    public None getGpgui() {
        return gpGUI;
    }

    public void setGpgui(None gpGUI) {
        this.gpGUI = gpGUI;
    }


}