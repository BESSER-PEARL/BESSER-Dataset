





import java.util.List;
import java.util.ArrayList;

public class ptn103_Place extends AbstractNode {






    private List<ptn103_AbstractNode> ptn103_abstractnodes;




    private ptn103_AbstractTransition ptn103_abstracttransition;




    private List<ptn103_AbstractTransition> ptn103_abstracttransitions;




    private List<ptn103_Token> ptn103_tokens;




    private List<ptn103_Place> ptn103_places;


    public ptn103_Place(
    ) {
        super(
        );
        this.ptn103_abstractnodes = new ArrayList<>();
        this.ptn103_abstracttransitions = new ArrayList<>();
        this.ptn103_tokens = new ArrayList<>();
        this.ptn103_places = new ArrayList<>();
    }

    public ptn103_Place(
        ArrayList<ptn103_AbstractNode> ptn103_abstractnodes,        ArrayList<ptn103_AbstractTransition> ptn103_abstracttransitions,        ArrayList<ptn103_Token> ptn103_tokens,        ArrayList<ptn103_Place> ptn103_places    ) {
        this.ptn103_abstractnodes = ptn103_abstractnodes;
        this.ptn103_abstracttransitions = ptn103_abstracttransitions;
        this.ptn103_tokens = ptn103_tokens;
        this.ptn103_places = ptn103_places;
    }


    public List<ptn103_AbstractNode> getPtn103_abstractnodes() {
        return ptn103_abstractnodes;
    }

    public void addPtn103_abstractnode(Ptn103_abstractnode ptn103_abstractnode) {
        this.ptn103_abstractnodes.add(ptn103_abstractnode);
    }
    public ptn103_AbstractTransition getPtn103_abstracttransition() {
        return ptn103_abstracttransition;
    }

    public void setPtn103_abstracttransition(ptn103_AbstractTransition ptn103_abstracttransition) {
        this.ptn103_abstracttransition = ptn103_abstracttransition;
    }
    public List<ptn103_AbstractTransition> getPtn103_abstracttransitions() {
        return ptn103_abstracttransitions;
    }

    public void addPtn103_abstracttransition(Ptn103_abstracttransition ptn103_abstracttransition) {
        this.ptn103_abstracttransitions.add(ptn103_abstracttransition);
    }
    public List<ptn103_Token> getPtn103_tokens() {
        return ptn103_tokens;
    }

    public void addPtn103_token(Ptn103_token ptn103_token) {
        this.ptn103_tokens.add(ptn103_token);
    }
    public List<ptn103_Place> getPtn103_places() {
        return ptn103_places;
    }

    public void addPtn103_place(Ptn103_place ptn103_place) {
        this.ptn103_places.add(ptn103_place);
    }

}