using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;
 
namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
       
        string os;
        int rb;
        int check = 0;
         
        private void button3_Click(object sender, EventArgs e)
        {
            button3.Visible = false;
            button1.Visible = true;
            button2.Visible = true;
            button5.Visible = true;
         }

        private void button4_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            button1.Visible = false;
            button2.Visible = false;
            button3.Visible = true;
            button5.Visible = false;
            if (check > 0)
            {
                string command = "killall";
                string argss = "-v VirtualBox";
                string verb = " ";
                ProcessStartInfo procInfo = new ProcessStartInfo();
                procInfo.WindowStyle = ProcessWindowStyle.Normal;
                procInfo.UseShellExecute = false;
                procInfo.FileName = command;   // 'sh' for bash 
                procInfo.Arguments = argss;        // The Script name 
                procInfo.Verb = verb;                 // ------------ 
                Process.Start(procInfo);
                check = 0;
            }
        
        }
        private void oscheck()
        {
            if (rb == 0)
            {
                os = "Fedora";
                rb = 1;
            }
            else if (rb == 1)
            {
                os = "Mint";
                rb = 2;
            }
            else if (rb == 2)
            {
                os = "MintC";
                rb = 3;
            }
            else if (rb == 3)
            {
                os = "OpenSuse";
                rb = 0;
            }
         
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string command = "python";
            string argss = "/home/rahil/Downloads/python/script.py ";
            string type = " Compute";
            string verb = "";
            oscheck();
            argss = argss + os + type;
            ProcessStartInfo procInfo = new ProcessStartInfo();
            procInfo.WindowStyle = ProcessWindowStyle.Normal;
            procInfo.UseShellExecute = false;
            procInfo.FileName = command;   // 'sh' for bash 
            procInfo.Arguments = argss;        // The Script name 
            procInfo.Verb = verb;                 // ------------ 
            Process.Start(procInfo);              // Start that proces
        }

      private void button2_Click(object sender, EventArgs e)
        {
            string command = "python";
            string argss = "/home/rahil/Downloads/python/script.py ";
            string type = " Storage";
            string verb = "";
            oscheck();   
            argss = argss + os + type;
            ProcessStartInfo procInfo = new ProcessStartInfo();
            procInfo.WindowStyle = ProcessWindowStyle.Normal;
            procInfo.UseShellExecute = false;
            procInfo.FileName = command;  
            procInfo.Arguments = argss;   
            procInfo.Verb = verb;         
            Process.Start(procInfo);      
            check = 1;
      }

      private void Form1_Load(object sender, EventArgs e)
      {

      }

    

      private void menuStrip1_ItemClicked(object sender, ToolStripItemClickedEventArgs e)
      {

      }

      private void toolStripMenuItem1_Click(object sender, EventArgs e)
      {

      }

      private void exitToolStripMenuItem_Click(object sender, EventArgs e)
      {
          Close();
      }

      private void newToolStripMenuItem_Click(object sender, EventArgs e)
      {
          Application.Restart();
      }

      private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
      {

      }

      private void restartToolStripMenuItem_Click(object sender, EventArgs e)
      {
          Application.Restart();
      }

      private void exitToolStripMenuItem_Click_1(object sender, EventArgs e)
      {
          Close();
      }

  
     }
   }
