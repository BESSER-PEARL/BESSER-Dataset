





import java.util.List;
import java.util.ArrayList;

public class domain_AreaRef  {

    private int group;





    private domain_Uielement domain_uielement;




    private domain_NickNamed domain_nicknamed;




    private domain_MenuItem domain_menuitem;


    public domain_AreaRef(
        int group    ) {
        this.group = group;
    }


    public int getGroup() {
        return group;
    }

    public void setGroup(int group) {
        this.group = group;
    }

    public domain_Uielement getDomain_uielement() {
        return domain_uielement;
    }

    public void setDomain_uielement(domain_Uielement domain_uielement) {
        this.domain_uielement = domain_uielement;
    }
    public domain_NickNamed getDomain_nicknamed() {
        return domain_nicknamed;
    }

    public void setDomain_nicknamed(domain_NickNamed domain_nicknamed) {
        this.domain_nicknamed = domain_nicknamed;
    }
    public domain_MenuItem getDomain_menuitem() {
        return domain_menuitem;
    }

    public void setDomain_menuitem(domain_MenuItem domain_menuitem) {
        this.domain_menuitem = domain_menuitem;
    }

}