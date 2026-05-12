





import java.util.List;
import java.util.ArrayList;

public class StartGame  {

    private int bidNumber;
    private int lead;
    private None deck;
    private None trick;
    private String playerOrder;
    private None t2;
    private None p3;
    private None t1;
    private None p2;
    private int turn;
    private None p1;
    private None p4;





    private List<Player> players;




    private List<Team> teams;




    private List<Trick> tricks;




    private List<Deck> decks;


    public StartGame(
        int bidNumber,        int lead,        None deck,        None trick,        String playerOrder,        None t2,        None p3,        None t1,        None p2,        int turn,        None p1,        None p4    ) {
        this.bidNumber = bidNumber;
        this.lead = lead;
        this.deck = deck;
        this.trick = trick;
        this.playerOrder = playerOrder;
        this.t2 = t2;
        this.p3 = p3;
        this.t1 = t1;
        this.p2 = p2;
        this.turn = turn;
        this.p1 = p1;
        this.p4 = p4;
        this.players = new ArrayList<>();
        this.teams = new ArrayList<>();
        this.tricks = new ArrayList<>();
        this.decks = new ArrayList<>();
    }

    public StartGame(
        int bidNumber,        int lead,        None deck,        None trick,        String playerOrder,        None t2,        None p3,        None t1,        None p2,        int turn,        None p1,        None p4        ArrayList<Player> players,        ArrayList<Team> teams,        ArrayList<Trick> tricks,        ArrayList<Deck> decks    ) {
        this.bidNumber = bidNumber;
        this.lead = lead;
        this.deck = deck;
        this.trick = trick;
        this.playerOrder = playerOrder;
        this.t2 = t2;
        this.p3 = p3;
        this.t1 = t1;
        this.p2 = p2;
        this.turn = turn;
        this.p1 = p1;
        this.p4 = p4;
        this.players = players;
        this.teams = teams;
        this.tricks = tricks;
        this.decks = decks;
    }

    public int getBidnumber() {
        return bidNumber;
    }

    public void setBidnumber(int bidNumber) {
        this.bidNumber = bidNumber;
    }
    public int getLead() {
        return lead;
    }

    public void setLead(int lead) {
        this.lead = lead;
    }
    public None getDeck() {
        return deck;
    }

    public void setDeck(None deck) {
        this.deck = deck;
    }
    public None getTrick() {
        return trick;
    }

    public void setTrick(None trick) {
        this.trick = trick;
    }
    public String getPlayerorder() {
        return playerOrder;
    }

    public void setPlayerorder(String playerOrder) {
        this.playerOrder = playerOrder;
    }
    public None getT2() {
        return t2;
    }

    public void setT2(None t2) {
        this.t2 = t2;
    }
    public None getP3() {
        return p3;
    }

    public void setP3(None p3) {
        this.p3 = p3;
    }
    public None getT1() {
        return t1;
    }

    public void setT1(None t1) {
        this.t1 = t1;
    }
    public None getP2() {
        return p2;
    }

    public void setP2(None p2) {
        this.p2 = p2;
    }
    public int getTurn() {
        return turn;
    }

    public void setTurn(int turn) {
        this.turn = turn;
    }
    public None getP1() {
        return p1;
    }

    public void setP1(None p1) {
        this.p1 = p1;
    }
    public None getP4() {
        return p4;
    }

    public void setP4(None p4) {
        this.p4 = p4;
    }

    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }
    public List<Team> getTeams() {
        return teams;
    }

    public void addTeam(Team team) {
        this.teams.add(team);
    }
    public List<Trick> getTricks() {
        return tricks;
    }

    public void addTrick(Trick trick) {
        this.tricks.add(trick);
    }
    public List<Deck> getDecks() {
        return decks;
    }

    public void addDeck(Deck deck) {
        this.decks.add(deck);
    }

}