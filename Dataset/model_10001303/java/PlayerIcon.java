





import java.util.List;
import java.util.ArrayList;

public class PlayerIcon  {

    private String icon;





    private BoardGUI boardgui;


    public PlayerIcon(
        String icon    ) {
        this.icon = icon;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }

    public BoardGUI getBoardgui() {
        return boardgui;
    }

    public void setBoardgui(BoardGUI boardgui) {
        this.boardgui = boardgui;
    }

}