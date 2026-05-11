





import java.util.List;
import java.util.ArrayList;

public class metamodeloArquitecturaPila_ListItem  {

    private String isSelected;
    private String action;





    private metamodeloArquitecturaPila_DropdownList metamodeloarquitecturapila_dropdownlist;


    public metamodeloArquitecturaPila_ListItem(
        String isSelected,        String action    ) {
        this.isSelected = isSelected;
        this.action = action;
    }


    public String getIsselected() {
        return isSelected;
    }

    public void setIsselected(String isSelected) {
        this.isSelected = isSelected;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public metamodeloArquitecturaPila_DropdownList getMetamodeloarquitecturapila_dropdownlist() {
        return metamodeloarquitecturapila_dropdownlist;
    }

    public void setMetamodeloarquitecturapila_dropdownlist(metamodeloArquitecturaPila_DropdownList metamodeloarquitecturapila_dropdownlist) {
        this.metamodeloarquitecturapila_dropdownlist = metamodeloarquitecturapila_dropdownlist;
    }

}